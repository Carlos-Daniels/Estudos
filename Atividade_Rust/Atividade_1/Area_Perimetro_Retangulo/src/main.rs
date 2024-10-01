/*
Faça um programa que, a partir das medidas dos lados de um retângulo, lidos via teclado,
calcule a área e o perímetro deste retângulo.
*/
use std::io;

fn main() {
    // Solicita ao usuário as medidas dos lados do retângulo
    println!("Digite a largura do retângulo: ");
    let mut largura = String::new();
    io::stdin().read_line(&mut largura).expect("Falha ao ler a entrada");

    println!("Digite a altura do retângulo: ");
    let mut altura = String::new();
    io::stdin().read_line(&mut altura).expect("Falha ao ler a entrada");

    //converte as entradas para números de ponto flutuante
    let largura : f64 = largura.trim().parse().expect("Por favor, insira um número válido");
    let altura : f64 = altura.trim().parse().expect("Por favor, digite um número válido");

    // Calcula a Area e o Perímetro
    let area = largura * altura;
    let perimetro = 2.0 * (largura * altura);

    // Exibe os resultados
    println!("A área do retângulo é: {:.2}", area);
    println!("O perimetro do retângulo é: {:.2}", perimetro);

}