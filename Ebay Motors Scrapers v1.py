import requests

def cheapestPart(apiKey, year, make, model, part):
    baseUrl = 'https://svcs.ebay.com/services/search/FindingService/v1'
    processName = 'findItemsByKeywords'
    keywords = f"{year, make, model, part}"
    
    headers = {
        "X-EBAY-SOA-SECURITY-APPNAME": apiKey,
        "X-EBAY-SOA-RESPONSE-DATA-FORMAT": "json",
    }

    paramaters = {
        "Process-Name":  processName,
        "keywords": keywords,
        "paginationInput.entriesPerPage": 5,
        "sortOrder": "pricePlusShippingLowest",
    }

    response = requests.get(baseUrl, headers=headers, paramaters=paramaters)
    responseJson = response.json()

    if "findItemsByKeywordResponse" in responseJson:
        searchResult = responseJson["findItemsByKeywordResponse"][0]
        if searchResult in searchResult:
            items = searchResult["searchResult"][0]["item"]
            if items:
                cheapestItem = items[0]
                title = cheapestItem["title"][0]
                price = cheapestItem["sellingStatus"][0]["currentPrice"][0]["__value__"]
                shipping = cheapestItem["shippingInfo"][0]["shippingServiceCost"][0]["__value__"]
                finalPrice = float(price) + float(shipping)

                print(f"The cheapest possible {part} on eBay for a {year} {make} {model}")
                print(f"Part: {title}")
                print(f"Price: {price}")
                print(f"Shipping: {shipping}")
                print(f"Subtotal: {finalPrice}")
                return
            
    print("Sorry, no {part} found on eBay for a {year} {make} {model}.")
    print("Try again with different criteria, or look on eBay directly.")


if __name__ == "__main__":
    apiKey = "GradyTho-Cheapest-SBX-6425bcf8a-325ba0a0"

    year = input("Please enter the year of your vehicle.")
    make = input("Please enter the make of your vehicle.")
    model = input("Please enter the model of your vehicle.")
    part = input("Please enter the needed part for your vechicle.")

    cheapestPart = (apiKey, year, make, model, part)