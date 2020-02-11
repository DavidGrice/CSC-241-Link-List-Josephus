from Linked_List import Linked_List

def Josephus(ll):
  # solve the Josephus problem following the following algorithm:
  # rotate the list to the left by one position circularly, 
  # and then delete the first element; 
  # repeat it until there is only one element left in the list.
  # print the sequence of survivors after each death, 
  # and finally print the survivor’s number.

  #Making sure there is only one victor!
  while(len(ll) != 1):
    #Kill the element next to the initial element
    ll.remove_element_at(2)
    #Rotate for the next element
    ll.rotate_left()
    #Print out the remaining 
    print(ll)


if __name__ == '__main__':
  n = int(input("Input the total number of people: "))
  # create a new doubly linked list object called ll
  # with n elements named 1 to n.
  ll = Linked_List()
  i = 1
  #Fill the linked list with elements
  while(i < n + 1):
    ll.append_element(i)
    i = i + 1
  #Print the Initial array
  print("Initial order:", ll)
  #Begin the Josephus problem
  Josephus(ll)
  #There is only one survivor
  print("The Survivor is:", ll.get_element_at(0))