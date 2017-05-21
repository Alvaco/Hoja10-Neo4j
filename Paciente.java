/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 *
 * Ana lucia Diaz
 */
public class Paciente{
    private String nombre;
    private String doctor;
    private int edad;
    private String Contrasena;
    
    public Paciente(String nombre,String Doctor,int edad,String Contrasena){ //revisen esta//
        this.nombre=nombre;
        this.edad=edad;
        this.Doctor=Doctor;
        this.Contrasena=Contrasena;
    }
    
    public void setNombre(String nombre){
        this.nombre=nombre;
    }
    
    public void setDoctor(String Doctor){
        this.carrera=carrera;
    }
    
    public void setEdad(int edad){
        this.edad=edad;
    }
    
    public void setContrasena(String contrasena){
        this.Contrasena=contrasena;
    }
    
    public String getNombre(){
        return nombre;
    }
    
    public String getDoctor(){
        return carrera;
    }
    
    public int getEdad(){
        return edad;
    }
    
    public String getContrasena(){
        return Contrasena;
    }
}
