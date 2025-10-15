
// Singleton
public class ClaseSingleton() {

    private static ClaseSingleton instance = null;

    private ClaseSingleton () {

    }

    public static ClaseSingleton getInstace(){
        if (instance == null){
            instance == new ClaseSingleton();
            return instance
        }
        return instance
    }

}


public class HelloWorld {
    public static void main(String[] args){
        //ClaseSingleton auxiliar = new ClaseSingleton()
        //Esto de arriba jamas lo ahremos en un Singleton

        ClaseSingleton.getInstace();
    }
}