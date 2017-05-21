/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * Ana lucia Diaz 
 */
public class Hospital{
    private String nombre;
    private String ubicacion;
    private String tipo;
    private String doctoresaservicio;
    
    public Hospitales(String nombre,String ubicacion,String tipo,String doctoresaservicio){
        this.nombre=nombre;
        this.ubicacion=ubicacion;
        this.tipo=tipo;
        this.doctoresaservicio=Doctoresaservicio;
    }
    
    public void setNombre(String nombre){
        this.nombre=nombre;
    }
    
    public void setUbicacion(String ubicacion){
        this.ubicacion=ubicacion;
    }
    
    public void setTipo(String tipo){
        this.tipo=tipo;
    }
    
    public void setDoctoresaservicioo(String doctoresaservicio){
        this.doctoresaservicio=doctoresaservicioo;
    }
    public String getNombre(){
        return nombre;
    }
    
    public String getUbicacion(){
        return ubicacion;
    }
    
    public String getTipo(){
        return tipo;
    }
    
    public String getDoctoresaservicioo(){
        return Doctoresaservicio;
    }
}
