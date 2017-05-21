import java.sql.*;


/**
 * Created by Ana lucia Diaz
 */
public class Connect {

    //Atributos
    private Connection con;
    private Statement stmt;
    private final String USER="neo4j";
    private final String PASSWORD= "neo4j1";
    static final String  _URL = "jdbc:neo4j:bolt://localhost";

    //constructor
    public Connect(){
        try{
            con = DriverManager.getConnection(_URL, USER,PASSWORD);
            stmt = con.createStatement();
        }
        catch(Exception e){
            System.out.println("Error");
        }
    }

    //Execute a query
    public ResultSet executeQuery(String query){
        ResultSet resultado = null;
        try{
            resultado = stmt.executeQuery(query);
        }catch(SQLException e){
            System.out.println("Error");
        }
        return resultado;

    }
    //See in an specific table the results
    public ResultSet getQuery(String _query){
        Statement state = null;
        ResultSet resultado = null;
        try{
            state = (Statement) con.createStatement();
            resultado = state.executeQuery(_query);
        }
        catch(SQLException e)
        {
            e.printStackTrace();

        }
        return resultado;
    }
    //History of queries
    public String History(ResultSet result){
        String cadena ="";

        try {

            while(result.next()){
                cadena += result.getString("n.name")+"\n";

            }
        }
        catch (SQLException e) {

            e.printStackTrace();
        }
        catch(NullPointerException  e1){

        }
        return cadena;

    }
    public void insert(String node,String id){
        try {
            stmt.executeUpdate("CREATE ("+node+": User{name:'"+ id+"'})");
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
    public void relate(String name1, String name2,String peso){
        try {
            stmt.executeUpdate("MATCH (x:User {name:'" + name1 + "'})" +"MATCH (y:User {name:'" + name2 + "'})" +"MERGE (x)-[:CORREOS {length: '" + peso + "'}]->(y)");
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
    public void delete(){
        try {
            stmt.executeUpdate("MATCH (n) " +
                    "OPTIONAL MATCH (n)-[r]-()"+" delete n,r" );
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
    public void simplificar(){


    }
}
