
Console.WriteLine("Операции: \r\n" +
    "1.сложение \r\n" +
    "2.вычитание \r\n" +
    "3.деление \r\n" +
    "4.умножение \r\n" +
    "5.возвести в степень \r\n" +
    "6.найти квaдратный корень из числа \r\n" +
    "7.найти 1 пpоцент от числа \r\n" +
    "8.найти факториал из числа \r\n" +
    "9.выйти из программы \r\n");
int Operation = 0;

while (Operation != 9)
{
     Operation = Convert.ToInt32(Console.ReadLine());

    if (Operation == 1)
    {
        Console.WriteLine("число 1");
        int a = Convert.ToInt32(Console.ReadLine());
        Console.WriteLine("число 2");
        int b = Convert.ToInt32(Console.ReadLine());
        Console.WriteLine(a + b);
    }
    if (Operation == 2)
    {
        Console.WriteLine("число 1");
        int a = Convert.ToInt32(Console.ReadLine());
        Console.WriteLine("число 2");
        int b = Convert.ToInt32(Console.ReadLine());
        Console.WriteLine(a - b);
    }
    if (Operation == 3)
    {
        Console.WriteLine("число 1");
        int a = Convert.ToInt32(Console.ReadLine());
        Console.WriteLine("число 2");
        int b = Convert.ToInt32(Console.ReadLine());
        Console.WriteLine(a / b);
    }
    else if (Operation == 4)
    {
        Console.WriteLine("число 1");
        int a = Convert.ToInt32(Console.ReadLine());
        Console.WriteLine("число 2");
        int b = Convert.ToInt32(Console.ReadLine());
        Console.WriteLine(a * b);
    }
    if (Operation == 5)
    {
        Console.WriteLine("введите число ");
        int a = int.Parse(Console.ReadLine());
        Console.WriteLine("введите степень ");
        int b = int.Parse(Console.ReadLine());
        Console.WriteLine(+Math.Pow(a, b));
    }
    else if (Operation == 6)
    {
        Console.WriteLine("введите число ");
        int a = int.Parse(Console.ReadLine());
        Console.WriteLine(+Math.Sqrt(a));
    }
    if (Operation == 7)
    {
        Console.WriteLine("введите число ");
        int a = Convert.ToInt32(Console.ReadLine());
        Console.WriteLine(a / 100);
    }
    else if (Operation == 8)
    {
        Console.WriteLine("введите число ");
        int a = Convert.ToInt32(Console.ReadLine());
        long fact = 1;
        int h1 = 5; // Факториал какого числа.
        if (fact == 0)
        {
            Console.WriteLine(1);
        }
        else
        {
            for (int i = 1; i <= h1; i++)
            {
                fact *= i;
            }
            Console.WriteLine(fact);
        }
    }

}
            
