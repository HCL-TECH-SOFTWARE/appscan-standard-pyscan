# Importing the regular expression package, and the appScan object
# import clr
import re
# import time
import __main__
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

def SearchForPattern(pattern, issueTypeName="User Defined Test", testName="SearchForPattern"):
    """Search the visited Urls for a patten,
    if found save it under a the supplied issue type.

    Example: SearchForPattern("\d{4}-\d{4}-\d{4}-\d{4}", "Credit Card Number")
    """

    # Get the issue type by its name
    issueType = GetIssueType(issueTypeName)

    # Iterate over all the visited Urls
    for visitedUrl in GetVisitedUrls():
        # For each Page, look for the pattern in it
        if Find(visitedUrl.Request.LogicalResponse, pattern):
            host = visitedUrl.Request.Uri.Host
            port = visitedUrl.Request.Uri.Port
            print("\r\nFound pattern on URL " + visitedUrl.Request.Uri.ToString() + "\r\n")

            # Save the result as an issue, on the relevant node in the tree                       
            objectId = ObjectID(int(visitedUrl.Request.GetHashCode() * random.random()))

            if issueType is not None:
                test = appScan.Scan.InsertNewVariant(visitedUrl.Request.DecodedUri, issueType.Name, issueType.Name,
                                                     SecurityData.EntityType.Link, testName,
                                                     SecurityData.TestTechnology.ManualTest, True, objectId, 0,
                                                     visitedUrl.Request.RawRequest, visitedUrl.Request.RawResponse,
                                                     visitedUrl.Request.RawRequest, visitedUrl.Request.RawResponse, "",
                                                     True)
            else:
                test = appScan.Scan.InsertNewVariant(visitedUrl.Request.DecodedUri, "attManualTest", "attManualTest",
                                                     SecurityData.EntityType.Link, testName,
                                                     SecurityData.TestTechnology.ManualTest, True, objectId, 0,
                                                     visitedUrl.Request.RawRequest, visitedUrl.Request.RawResponse,
                                                     visitedUrl.Request.RawRequest, visitedUrl.Request.RawResponse, "",
                                                     True)
            # Add a comment to the issue
            issue = test.GetIssue(AppScan.Scan.Data.TreeViewType.UrlBased)
            for issueImage in issue.ImageGallery:
                if issueImage.VariantId is test.Id:
                    issueImage.Comments = "Pattern " + pattern + " found on this URL (found using Pyscan)"
        else:
            # For progress indication, print a dot
            print(".")


def FuzzRequest(request, minValue, maxValue, matchPattern, host=None, port=None, issueTypeName="User Defined Test",
                placeHolder="<fuzz here>", testName="FuzzRequest"):
    """
    Perform fuzzing on a request using a place holder (by default '<fuzz here>').
    The placeholder is replaced with each value in the given range, and the given pattern is looked for in each response.
    If matched, the request is saved to as the given issue type.
    If no host and port are supplied, the starting URL's host and port are used.
    
    Example: FuzzRequest(fuzzDemoReq, 95,105, "200 OK")
    """

    # If we don't have a host and port, read them from the starting URL
    try:
        startingUri = System.Uri(appScan.Scan.ScanData.Config.StartingUrl)
    except:
        print("an Error occurred while trying to read startingUri.\nplease make sure you've configured a starting URL")
    if host is None:
        host = startingUri.Host
    if port is None:
        port = startingUri.Port

    # Get the root node
    path = ""
    for visitedUrl in GetVisitedUrls():
        path = visitedUrl.Request.DecodedUri
        break

    # Get the issue type object for the given issue type
    issueType = GetIssueType(issueTypeName)
    # Enumerate the values in the supplied range
    for i in range(minValue, maxValue):

        # Print the numbers for visual progress indication
        print(str(i)+":")

        # Replace the placeholder with the current value in the range
        fuzzedRequest = request.replace(placeHolder, str(i))
        print("fuzz request processing...")
        # Submit the test request (AppScan will handle all communication and test environment issues)
        null = ""
        result, response = appScan.Scan.SendManualTest(fuzzedRequest, host, port, True if port == 443 else False, True,
                                                       null)
        if result:
            print("got a response, searching for success pattern...")
        # Some sites may not handle the load of a quick sequence of requests
        # If that's the case, a sleep command between tests could prove useful
        # time.sleep(1)

        # If the given pattern was found in the response, save the test request as a found issue               
        if result is True and Find(response, matchPattern):
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
                    issueImage.Comments = "Pattern '" + matchPattern + "' found when testing value " + str(
                        i) + " in range of " + str(minValue) + " - " + str(maxValue) + " (found using Pyscan)"
                    print(issueImage.Comments)
        else:
            print("no success pattern was found :(\n\n")


# This demo request is used to demonstrate the use of the FuzzRequest function
# on the demo site http://demo.testfire.net/
# noinspection SpellCheckingInspection
fuzzDemoReq = """POST /bank/doTransfer HTTP/1.1 \r\n
User-Agent: Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36\r\n
Referer: https://demo.testfire.net/bank/transfer.jsp\r\n
Cookie: AltoroAccounts="ODAwMDAyflNhdmluZ3N+MS42NDQ3MjAwNjcwOTY2MTMzRTE5fDgwMDAwM35DaGVja2luZ34xLjE4NDQ2NzQ0MDgzNzY1OTJFMjB8NDUzOTA4MjAzOTM5NjI4OH5DcmVkaXQgQ2FyZH4tMS45OTk1NDM0MjQ3MTIxMzUxN0UxOHw="; JSESSIONID=EDA28EB3A82D1E841AFD9D8E28A016FD\r\n
Host: demo.testfire.net\r\n
Content-Length: 79\r\n
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n
Accept-Language: en-US\r\n
Content-Type: application/x-www-form-urlencoded\r\n\r\n
fromAccount=800003<fuzz here>&toAccount=800003&transferAmount=1234&transfer=Transfer+Money
"""

print("Pyscan Utils Loaded")

# uncomment below lines to test functionality
# for visitedUrl in GetVisitedUrls():
# 	print(visitedUrl.Request.Uri.ToString())
# SearchForPattern("\w", "AltoroAccounts")

FuzzRequest(fuzzDemoReq, 95, 105, matchPattern="HTTP....\s200")
