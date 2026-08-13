package Projeto_cobrinha;

import Projeto_cobrinha.generico.Box;

public class Main {
    public static void main (String [] args){
        Box<String> b = new Box<>();
        
        b.setItem("Teste");
        b.getItem();

         Box<Integer> a = new Box<>();
         a.setItem(2);
         a.getItem();
    }
}
