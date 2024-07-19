
import string

def pass_checker():

    lower=string.ascii_lowercase

    upper=string.ascii_uppercase

    digit=string.digits

    symbol=string.punctuation

    print(__name__)

    while True:

        n=input('Enter Password')

        l=[0,0,0,0,0]

        for i in  n:

            if i in lower:

                l[0]=1

            elif i in upper:

                l[1]=1

            elif i in digit:

                l[2]=1

            elif i in symbol:

                l[3]=1
 
        if len(n)>=8:

            l[-1]=1

        if sum(l)==5:

            print('Password is Strong')
            return n

            break

        else:

            print('Password is not strong')

            i=0

            while i<5:

                if l[i]==0:

                    if i==0:

                        print('Add Lower Characters')

                    if i==1:

                        print('Add Upper Character')

                    if i==2:

                        print('Add Digit')

                    if i==3:

                        print('Add Symbol')

                i+=1

            if len(n)<8:

                print('Password length is small')

if __name__=='__main__':

    pass_checker()
