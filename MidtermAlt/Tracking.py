# Using the tracking.xml file, complete the following:
# Output the total number of orders (using the XML element)
# Output the total number of products
# For each order, please print the following:
#    - The Order Id
#    - The warehouse it was shipped from
#    - The total amount
#    - The tracking number
#    - The carrier
#    - Whether the order was delivered
#    NOTE: If any of the above is not available, print 'N/A'

import xml.etree.ElementTree as EL

try:
    xml_file = 'tracking.xml'
    tree = EL.parse(xml_file)

    orders = tree.findall('Order')
    print("The total number of orders is: "+tree.find('TotalOrders').text)
    print("The total number of products: "+tree.find('TotalProducts').text)

    print("\nThe information on the orders is:")
    for order in orders:
        print("The Order ID is: "+order.attrib['id'])
        print("The warehouse: "+order.attrib['warehouse'])
        if order.attrib['affiliateStatus'] != 'canceled':
            print("Total is: "+order.attrib['total'])
        else:
            print("Total is: N/A")

        tracking = order.find('TrackingNumber')
        if tracking is not None:
            print("The tracking number is: "+tracking.text.strip())
            print("The carrier is: "+tracking.attrib['carrier'])
            print("Has the order been delivered: "+tracking.attrib['delivered'])
        else:
            print("Tracking number is: N/A")
            print("The carrier is: N/A")
            print("Has the order been delivered: N/A")

        print()
except:
    print("An error occurred")
