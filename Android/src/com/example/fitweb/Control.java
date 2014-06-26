package com.example.fitweb;

public class Control
{
	String tipo;
	String nombre;
	float valor;
	String fecha;
	public Control(String ti,String no,float val,String fe)
	{
		tipo=ti;
		nombre=no;
		valor=val;
		fecha=fe;
	}
	public float getValor()
	{
		return valor;
	}
	public String getFecha()
	{
		return fecha;
	}
	public String getNombre()
	{
		return nombre;
	}
	public String getTipo()
	{
		return tipo;
	}
	public void setValor(float val)
	{
		this.valor=val;
	}
	public void setFecha(String fe)
	{
		this.fecha=fe;
	}
	public void setNombre(String no)
	{
		this.nombre=no;
	}
	public void setTipo(String ti)
	{
		this.tipo=ti;
	}
}
