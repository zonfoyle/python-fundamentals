"""This script demonstrated the use of PYthon functions.
The create_shoe function takes a list of materials as input and 
determines the type of shoe created on those materials."""
def main ():
    #Determine the type of shoe created based on materials
    materials_1 = ['leather', 'rubber']
    materials_2 = ['canvas', 'rubber']
    materials_3 = ['mesh', 'rubber']

    #Use the create_shoe functon and check the results 
    shoe = create_shoe(materials_1)
    shoe_2 = create_shoe(materials_2)
    shoe_3 = create_shoe(materials_3)

    print(f"Shoes is of type: {shoe['type']}")
    print(f"Shoes is of type: {shoe_2['type']}")
    print(f"Shoes is of type: {shoe_3['type']}")

def create_shoe(materials_list):
     shoe_type = ''

     if 'leather' in materials_list and 'rubber' in materials_list:
        shoe_type = 'boots'
     elif 'mesh' in materials_list and 'rubber' in materials_list:
         shoe_type = 'sneakers'
     else: 
         shoe_type = 'unknown'

     return {'type': shoe_type}



if __name__ == "__main__":
     main()