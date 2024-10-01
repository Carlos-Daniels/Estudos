/*
Leia o tamanho do lado de um quadrado e imprima como resultado a sua área.
*/

use std::io;

fn main(){
    println!("Digite a medida lateral do quadrado: ");

    let mut lado = String::new();
    io::stdin().read_line(&mut lado).expect("Falha ao ler a entrada");

    let lado: f64 = lado.trim().parse().expect("Por favor, insira um número valido");

    let area = lado * lado;

    println!("A area do quadrado é {:.2}", area);
}