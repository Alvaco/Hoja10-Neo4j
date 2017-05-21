import java.sql.*;
import java.util.HashSet;
import java.util.Map;

public class Conexion {
    private Connection con;
    private Statement stmt;
    private final String USER="neo4j";
    private final String PASSWORD="neo4j1";
    static final String URL="jdbc:neo4j:bolt://localhost";
    
    //constructor
    public Conexion(){
        try{
            con= DriverManager.getConnection(URL,USER,PASSWORD);
            stmt=con.createStatement();
        }
        catch(Exception e){
            System.out.println("Error");
        }
    }
    
    public void crearPaciente(Paciente e1){
        try{
            stmt.executeUpdate("CREATE(" +e1.getNombre()+ ":Paciente{name:'" +e1.getNombre()+ "',doctor:'" +e1.getDoctor()+ "',edad:'" +e1.getEdad()+"'})");
        }
        catch (SQLException e) {
            e.printStackTrace();
        }
    }
    
    
    public void crearHospital(Hospital r){
        try{
            stmt.executeUpdate("CREATE("+r.getNombre()+":Hospital{name:'"+r.getNombre()+"',tipo:'"+r.getTipo()+"',ubicacion:'"+r.getUbicacion()+"',medicamento:'"+r.getMedicamento()+"'})");
        }
        catch (SQLException e) {
            e.printStackTrace();
        }
    }
    
    public void crearDoctor(Paciente e1, Hospital r){
        try{
            stmt.executeUpdate("MATCH (x:Paciente {name:'"+ e1.getNombre()+"'})MATCH (y:Hospital{name:'"+r.getNombre()+"'})"+"MERGE (x)-[:Medicamento]->(y)");
        }
        catch (SQLException e) {
            e.printStackTrace();
        }
    } 
    
    public void deletePaciente(Paciente e1){
        try {
            stmt.executeUpdate("MATCH (x:Paciente{name:'"+e1.getNombre()+"'}) detach delete x");
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
    
    public void deleteHospital(Restaurante r1){
        try {
            stmt.executeUpdate("MATCH (x:Hospital{name:'"+r1.getNombre()+"'}) detach delete x");
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
    
    public void crearPacienter(Paciente e1,Paciente e2){
        try{
            stmt.executeUpdate("MATCH (x:Paciente {name:'"+ e1.getNombre()+"'})MATCH (y:Paciente{name:'"+e2.getNombre()+"'})"+"MERGE (x)-[:pacienter]->(y)");
        }
        catch (SQLException e) {
            e.printStackTrace();
        }
    }
    
    public void getPaciente(String nombre){
        try{
            ResultSet rs = stmt.executeQuery("MATCH (Paciente{name:"+nombre+"})-[rel:pacienter]-(pacienter) return Pacienter");
            Map map= (Map)rs.getObject("Pacienter");
            String s=map.get("name").toString();
        }
        catch (SQLException e) {
            e.printStackTrace();
        }
    }
    
    public String[] Recomendar(Paciente e1){
        String [] respuesta=new String[3];
        String[] res=new String[1000];
        String[] totalHospitales=new String[1000];
        try{
            ResultSet rs = stmt.executeQuery("MATCH (Pacientes{name:'"+e1.getNombre()+"'})-[rel:pacientesr]-(pacientesr) return Pacientesr");
            int i=0;
            while (rs.next()){
                Map map = (Map)rs.getObject("Pacientesr");
                String s = map.get("name").toString();
                System.out.println(s);
                res[i]=s;
                    //tomando los restaurantes
                    ResultSet tesRest=stmt.executeQuery("MATCH (Paciente{name:'"+s+"'})-[rel:Doctor]-(Hospital) return Hospital");
                    while(tesRest.next()){
                        Map tempMap=(Map)tesRest.getObject("Hospital");
                        String t=tempMap.get("name").toString();
                        totalHospitales[i]=t;
                        System.out.println(t);
                    }
                i++;
            }          
        }
        catch (SQLException e) {
            e.printStackTrace();
        }
        //agregando en el hashset
        HashSet tempSet=new HashSet();
        for(int m=0;m<totalHospitales.length;m++){
            String nombreRes=totalHospitales[m];
            tempSet.add(nombreRes);
        }
        
        int[] frecuencias=new int[10];
        for(int q=0;q<frecuencias.length;q++)
            frecuencias[q]=0;
        
        String[] orden=new String[10];
        
        //obteniendo frecuencias
        int count=0;
        for(int n=0;n<res.length;n++){
            if(tempSet.contains(res[n])){
                frecuencias[count]=+1;
                orden[count]=res[n];
            }
        }
        
        for(int q=0;q<orden.length;q++)
            System.out.print(orden[q]);
        
        System.out.println();
        
        for(int q=0;q<frecuencias.length;q++)
            System.out.print(frecuencias[q]);
        
        System.out.println(orden[0]);
        return orden;
        
    }
        
  
}
