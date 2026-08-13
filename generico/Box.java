package Projeto_cobrinha.generico;

public class Box<T> {
    
    private T item;

    public void getItem() {
        System.out.println(this.item);
    }
    public void setItem(T i) {
        this.item = i;
    } 
}
