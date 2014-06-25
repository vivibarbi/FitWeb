package com.example.fitweb;

public class DataBaseManager
{
	
	public static final String TABLE_NAME1="Actividades";
		
		public static final String Ac_id="Id_Ac";
		public static final String Ac_ti="Tipo";
		public static final String Ac_no="Nombre";
		public static final String Ac_val="Valor";
	
	public static final String TABLE_NAME2="Control";
		public static final String Co_id="Id_Co";
		public static final String Co_Val_Cal="Valor Calorias";
		public static final String Co_Fe="Fecha";
		public static final String Co_Ac="Id_Ac";
		/*
		 * create talbe contactos(
		 * 							_id integer primary key autoincrement,
		 * 							nombre text not null,
		 * 							telefono text);
		 * 
		 */
		
		public static final String CREATE_TABLE ="create table "+TABLE_NAME1+" ("
				+ Ac_id+" integer primary key autoincrement,"
				+ Ac_ti+" text not null,"
				+ Ac_no+" text not null,"
				+ Ac_val+" real);";
		
		public static final String CREATE_TABLE2 ="create table "+TABLE_NAME2+" ("
				+ Co_id+" integer primary key autoincrement,"
				+ Co_Val_Cal+" real,"
				+ Co_Fe+" TIMESTAMP NOT NULL DEFAULT current_timestamp ,"
				+ Co_Ac+" integer);";

}
