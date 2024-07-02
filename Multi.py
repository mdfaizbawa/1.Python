class Multifunctions():
    def OddEven():
        num=int(input("Enter a number:"))
        if((num%2)==1):
            print(num,"is odd number")
        else:
            print(num,"is Even number")

    def Eligible():
      gender=input("Your Gender:")
      age=int(input("Your Age:"))
      if(gender=="Male" and age>21):
        print("ELIGIBLE")
      elif(gender=="Female" and age>18):
        print("ELIGIBLE")
      else:
        print("NOT ELIGIBLE")

    def percentage():
      sub1=int(input("Subject1="))
      sub2=int(input("Subject2="))
      sub3=int(input("Subject3="))
      sub4=int(input("Subject4="))
      sub5=int(input("Subject5="))
      total=sub1+sub2+sub3+sub4+sub5
      print("Total=",total)
      per=float(total)*100/500
      print("Percentage:",per)

    def triangle():
      Height=int(input("Height:"))
      Breadth=int(input("Breadth:"))
      print("Area formula:(Height*Breadth)/2")
      Area=((Height*Breadth)/2)
      print("Area of Triangle:",Area)
      Height1=int(input("Height1:"))
      Height2=int(input("Height2:"))
      Breadth1=int(input("Breadth:"))
      print("Perimeter formula:Height1+Height2+Breadth")
      perimeter=(Height1+Height2+Breadth1)
      print("Permeter of Triangle:",perimeter)