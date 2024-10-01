/*
Crie um programa que permita fazer a conversão cambial entre Dólares e Reais. Considere
como taxa de câmbio US$ 1,00 = R$5,27. Leia um valor em Dólares pelo teclado e mostre o
correspondente em Reais.
*/
use std::io;

fn main(){
    const TAXA: f64 = 5.27;

    // Solicita ao usuário um valor em dólares
    println!("Digite o valor em dólares: ");

    //cria uma variavel para armazenar a entrada do usuário
    let mut dolares = String::new();

    // Lê o valor inserido
    io::stdin().read_line(&mut dolares)
    .expect("Falha ao ler a entrada");

    // Converte a string para um número flutuante
    let dolares: f64 = dolares.trim().parse()
    .expect("Por favor, digite um número válido");

    // Faz a conversão de Dólares para Reais
    let reais = dolares * TAXA;
    
    // Exibe o valor correspondente em Reais
    println!("O valor correspondente em Reais é: R${:.2}", reais);
}