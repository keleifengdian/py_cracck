    #include <stdio.h>  
    #include <unistd.h>  
      
    int main()  
    {  
            printf("Encrypted: %s\n", crypt("111111", "$6$nrfRImA/$"));  
            return 0;  
    }  
