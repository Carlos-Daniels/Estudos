/*
Leia um número inteiro e imprima o seu antecessor e o seu sucessor.
*/

use std::io;

fn main(){
    // Solicita para digitar um numero inteiro
    println!("Digite um número inteiro: ");
    let mut numero = String::new();

    io::stdin().read_line(&mut numero).expect("Por favor, insira um número inteiro valido");

    // Converter a string para numero inteiro
    let numero: i32 = numero.trim().parse().expect("Por favor, insira um número inteiro valido");

    // Calcula o antecessor e sucessor
    let antecessor = numero - 1;
    let sucessor = numero + 1;

    // Exibe o antecessor e o sucessor 
    println!("O antecessor de {} é {}", numero, antecessor);
    println!("O sucessor de {} é {}", numero, sucessor);
}
