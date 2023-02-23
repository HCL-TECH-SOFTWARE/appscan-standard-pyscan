#######################################################################################################################
# Licensed Materials �Property of HCL Technologies Ltd.
# � Copyright HCL Technologies Ltd. 2022.
# All rights reserved. See product license for details. US Government Users Restricted Rights. Use, duplication,
# or disclosure restricted by GSA ADP Schedule Contract with HCL Technologies Ltd. Java and all Java-based trademarks
# and logos are trademarks or registered trademarks of Oracle and/or its affiliates. HCL, the HCL logo,
# and Tivoli are registered trademarks of HCL Technologies in the United States, other countries, or both.
#######################################################################################################################
# Importing the regular expression package, and the appScan object
# import clr
import re
# import time
import __main__
import sys

from DBAdapter import ObjectID
from CLR import SecurityData
import random

appScan = __main__.appScan


# Utility Functions
####################

def GetVisitedUrls():
    # "Returns all the visited Urls in the current scan as a iterator"
    appData = appScan.Scan.ScanData.GetAppTreeRoot(AppScan.Scan.Data.TreeViewType.UrlBased).GetApplicationData()
    return iter(appData.VisitedUrls)


def GetTreeNode(url):
    # "Gets the tree node that matches the given URL"

    for node in appScan.Scan.ScanData.GetAppTreeRoot(AppScan.Scan.Data.TreeViewType.UrlBased).DescendentUrls:
        if node.Path == url:
            return node

    return None


def Find(string, pattern):
    """Returns true if the regex pattern is found within the string"""

    return re.search(pattern, string, re.I | re.S | re.M) is not None


def GetIssueType(issueTypeName):
    """Gets an IssueType element according to the giving issueTypeName string
    The IssueType element can be used with the appScan.Scan.SendManualTest method
    """

    # Get al issue types that partially match the name
    issueTypes = appScan.Scan.ScanData.Config.TestPolicy.IssueTypes
    values = iter(issueTypes.Dictionary.Values)

    # Iterate over all of them, trying to get a match
    foundIssueType = None
    for v in values:
        # Check if a partial match was found
        if v.RulesIssueType.Description.__contains__(issueTypeName):
            foundIssueType = v.RulesIssueType

            # If an exact match was found - use that
            if v.RulesIssueType.Description == issueTypeName:
                return foundIssueType

    return foundIssueType


# Sample Pyscan uses
###############################################

def MultiplePayloads(payloads, urlsToCheck=set(), matchPattern=None, issueTypeName="User Defined Test",
                     placeHolder="<fuzz here>", testName="UserDefinedTest_MultiplePayloads"):
    """
    Perform fuzzing on a request using a place holder (by default '<fuzz here>').
    The placeholder is replaced with each value in the given payloads list,
    and the given pattern is looked for in each response.
    If matched, the request is saved to as the given issue type.
    If no host and port are supplied, the starting URL's host and port are used.
    If the urlsToCheck set is empty this will be performed on all visited URLs, otherwise only visited URLs in this set.

    Example: MultiplePayloads(payloads=["udt1", "udt2", "udt3"], urlsToCheck={"https://demo.testfire.net/feedback.jsp"},
                     matchPattern="HTTP....\s200", placeHolder="Gecko")
    """

    # Get the root node
    path = str(System.Uri(appScan.Scan.ScanData.Config.StartingUrl))

    # Get the issue type by its name
    issueType = GetIssueType(issueTypeName)

    # Iterate over all the visited Urls
    for visitedUrl in GetVisitedUrls():
        uri = visitedUrl.Request.Uri

        # If the given list of URLs is not empty and doesn't contain the current URL we skip to the next URL
        if urlsToCheck and str(uri) not in urlsToCheck:
            continue
        request = visitedUrl.Request.RawRequest
        host = uri.Host
        port = uri.Port

        # Enumerate the values in the supplied payloads
        for payload in payloads:
            # Print the current payload and URL
            print("URL: " + str(uri) + "\tPayload: " + payload)

            # Only perform attacks if we actually can modify the request
            if placeHolder not in request:
                print("\t" + str(uri) + " does not contain \"" + placeHolder + "\", skipping testing...")
                continue

            # Replace the placeholder with the current value in the range
            fuzzedRequest = request.replace(placeHolder, payload)
            # Submit the test request (AppScan will handle all communication and test environment issues)
            null = ""
            result, response = appScan.Scan.SendManualTest(fuzzedRequest, host, port, True if port == 443 else False,
                                                           True, null)

            if result:
                print("got a response, searching for success pattern...")
            # Some sites may not handle the load of a quick sequence of requests
            # If that's the case, a sleep command between tests could prove useful
            # time.sleep(1)

            # If the given pattern was found in the response, save the test request as a found issue
            if result is True and matchPattern is not None and Find(response, matchPattern):
                print(" - Pattern Matched - Saved as issue.\n\n")

                # Save the result as an issue
                objectId = ObjectID(int(id(fuzzedRequest) * random.random()))

                if issueType:
                    test = appScan.Scan.InsertNewVariant(path, issueType.Name, issueType.Name, SecurityData.EntityType.Link,
                                                         testName,
                                                         SecurityData.TestTechnology.ManualTest, True, objectId, 0, request,
                                                         "",
                                                         fuzzedRequest, response, "", True)
                else:
                    test = appScan.Scan.InsertNewVariant(path, "attManualTest", "attManualTest",
                                                         SecurityData.EntityType.Link, testName,
                                                         SecurityData.TestTechnology.ManualTest, True, objectId, 0, request,
                                                         "",
                                                         fuzzedRequest, response, "", True)
                    # Add a comment to the issue
                issue = test.GetIssue(AppScan.Scan.Data.TreeViewType.UrlBased)
                for issueImage in issue.ImageGallery:
                    if issueImage.VariantId == test.Id:
                        issueImage.Comments = "Pattern '" + matchPattern + "' found when testing value " + payload + " (found using Pyscan)"
                        print(issueImage.Comments)
            else:
                print("no success pattern was found :(\n\n")


print("Pyscan Utils Loaded")

try:
    # Will attempt to attack all visited URLs with all payloads by replacing the phrase "<fuzz here>" with a payload.
    # Will probably not find any issues as there are probably not any requests containing "<fuzz here>"
    # and no verification will ever be attempted anyway as long as matchPattern is None
    #MultiplePayloads(payloads=["udt1", "udt2", "udt3"], urlsToCheck=set(), matchPattern=None, placeHolder="<fuzz here>")

    # Will attempt to attack all visited URLs that are also defined in urlsToCheck with all payloads by replacing
    # the phrase "Gecko" with a payload.
    # Will probably find many issues as there are probably many requests containing "Gecko"
    # and all the verification does it make sure the response contains the regular expression matchPattern
    # (which in this case is HTTP response code of 200).
    MultiplePayloads(payloads=["udt1", "udt2", "udt3"], urlsToCheck={"https://demo.testfire.net/feedback.jsp"},
                     matchPattern="HTTP....\s200", placeHolder="Gecko")
except Exception as e:
    print(e)
