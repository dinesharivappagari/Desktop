import java.util.Scanner;
public class Program {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int dated = sc.nextInt();
        
        int enddate = 2024;
        int count = 0;
        
        for (int i = dated + 1; i <= enddate; i++) {
            count++;
        
        } 
          
          //your born year like 2010
          
          
       String text ="you are "+count+" years old";
            
        System.out.println("year:"+dated);
        System.out.println(text);
        System .out.println("Age:"+count);
        
    }
}

