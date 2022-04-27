fn is_prime(num: i128) -> bool{
    println!("Starting Check for {}", num);
    for i in 2..num {
        if i == num {
            continue
        } else if num%i == 0 {
            println!("Number is not prime...skipping");
            return false;
        }
    }
    println!("Number is prime!");
    return true;
}

fn fibbo_prime(limit: i128) -> Vec<i128> {
    let mut fibbo = Vec::new();
    
    let mut term1 = 1;
    let mut term2 = 1;
    let mut temp = 0;
    let mut count = 0;

    while count < limit {
        temp = term1;
        term1 = term2;
        term2 = term2 + temp;

        println!("Currently at {} primes", count);
        println!("Scanning {}", term2);

        if is_prime(term2) {
            count = count + 1;
            fibbo.push(term2);
        }
    }

    println!("Sucess!");
    return fibbo;
}

fn main() {
    // get required nums
    let fibbo = fibbo_prime(10);
    
    println!("{:?}", fibbo);
    println!("Compiled and generated first 10 fibbonacci primes");
    println!("Amount of primes left: 24");

    let mut line = String::new();

    std::io::stdin()
        .read_line(&mut line);

    // get theoretical nums
    println!("{:?}", fibbo_prime(20));
}