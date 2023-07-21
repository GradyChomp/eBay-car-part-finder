import requests

def cheapestPart(apiKey, year, make, model, part):
    baseUrl = 'https://svcs.ebay.com/services/search/FindingService/v1' #don't know if this is even right
    processName = 'findItemsByKeywords'
    keywords = f"{year}, {make}, {model}, {part}" #now uses values instead of name
    
    headers = {
      "X-EBAY-SOA-SECURITY-APPNAME": apiKey,
      "X-EBAY-SOA-RESPONSE-DATA-FORMAT": "json",
      "X-EBAY-C-MARKETPLACE-ID": "EBAY-US",  # Adding a valid marketplace ID (for US)
      "X-EBAY-C-ENDUSERCTX": "affiliateCampaignId=5338432561",  # Adding a sample end user context
    }
    
    paramaters = {
        "OPERATION-NAME":  processName,
        "keywords": keywords,
        "paginationInput.entriesPerPage": 5,
        "sortOrder": "pricePlusShippingLowest",
    }

    response = requests.get(baseUrl, headers=headers, paramaters=paramaters)
    responseJson = response.json()

    if "findItemsByKeywordsResponse" in responseJson:
        searchResult = responseJson["findItemsByKeywordsResponse"][0]
        items = searchResult.get("searchResult", {}).get("item", [])
        if items:
                cheapestItem = items[0]
                title = cheapestItem["title"]
                price = cheapestItem["sellingStatus"]["currentPrice"]["__value__"]
                shipping = cheapestItem["shippingInfo"]["shippingServiceCost"]["__value__"]
                finalPrice = float(price) + float(shipping)

                print(f"The cheapest possible {part}s on eBay for a {year} {make} {model}:")
                print(f"Part: {title}")
                print(f"Price: {price}")
                print(f"Shipping: {shipping}")
                print(f"Subtotal: {finalPrice}")
                return
            
    print("Sorry, no {part} found on eBay for a {year} {make} {model}.")
    print("Try again with different criteria, or look on eBay directly.")


if __name__ == "__main__":
    apiKey = "GradyTho-Cheapest-SBX-6425bcf8a-325ba0a0"

    year = int(input("Please enter the year of your vehicle."))
    make = input("Please enter the make of your vehicle.")
    model = input("Please enter the model of your vehicle.")
    part = input("Please enter the needed part for your vechicle.")

    cheapestPart(apiKey, year, make, model, part) #calling function instead of naming it :(