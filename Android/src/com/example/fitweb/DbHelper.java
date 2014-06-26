package com.example.fitweb;

import java.util.ArrayList;
import java.util.List;



import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;
import android.database.sqlite.SQLiteDatabase.CursorFactory;




	public class DbHelper extends SQLiteOpenHelper {
		String tipo=MainActivity.aux;
		String nombre=MenuDeportes.aux_nom;

		private static final String DB_NAME="fitwebDB.sqlite";
		private static final int DB_SCHEME_VERSION=1;
		public DbHelper(Context context) {
			super(context, DB_NAME, null, DB_SCHEME_VERSION);
			// TODO Auto-generated constructor stub
		}
		/*public DbHelper(Context cont,String nombre
				,CursorFactory fact,int version)
		{
			super(cont,nombre,fact,version);
		}*/
		
		
		@Override
		public void onCreate(SQLiteDatabase db) {
			
			db.execSQL(DataBaseManager.CREATE_TABLE);
			db.execSQL(DataBaseManager.CREATE_TABLE2);
			db.beginTransaction();
			try
			{
				//db.execSQL("SELECT COUNT(*) FROM contactos");
				//System.out.println("Jalaaaaaaaa");
				//ContentValues values=new ContentValues();
				
				db.execSQL("insert into Actividades(Tipo,Nombre,Valor) values("+"'"+"Deportes"+"'"+",'"+"Básquetbol Moderado"+"',"+"0.099)");
				db.execSQL("insert into Actividades(Tipo,Nombre,Valor) values("+"'"+"Deportes"+"'"+",'"+"Básquetbol Vigoroso"+"',"+"0.1562)");
				db.execSQL("insert into Actividades(Tipo,Nombre,Valor) values("+"'"+"Deportes"+"'"+",'"+"Bicicleta Vel. Baja"+"',"+"0.1078)");
				db.execSQL("insert into Actividades(Tipo,Nombre,Valor) values("+"'"+"Deportes"+"'"+",'"+"Bicicleta Vel. Moderada"+"',"+"0.1562)");
				db.execSQL("insert into Actividades(Tipo,Nombre,Valor) values("+"'"+"Deportes"+"'"+",'"+"Básquetbol Moderado"+"',"+"0.099)");
				db.execSQL("insert into Actividades(Tipo,Nombre,Valor) values("+"'"+"Deportes"+"'"+",'"+"Boxeo Moderado"+"',"+"0.1144)");
				db.execSQL("insert into Actividades(Tipo,Nombre,Valor) values("+"'"+"Deportes"+"'"+",'"+"Boxeo Vigoroso"+"',"+"0.1716)");
				db.execSQL("insert into Actividades(Tipo,Nombre,Valor) values("+"'"+"Deportes"+"'"+",'"+"Caminata Moderada"+"',"+"0.0638)");
				db.execSQL("insert into Actividades(Tipo,Nombre,Valor) values("+"'"+"Deportes"+"'"+",'"+"Caminata Vigorosa"+"',"+"0.1056)");
				db.execSQL("insert into Actividades(Tipo,Nombre,Valor) values("+"'"+"Deportes"+"'"+",'"+"Fútbol Moderado"+"',"+"0.1144)");
				db.execSQL("insert into Actividades(Tipo,Nombre,Valor) values("+"'"+"Deportes"+"'"+",'"+"Fútbol Vigoroso"+"',"+"0.2134)");
				db.execSQL("insert into Actividades(Tipo,Nombre,Valor) values("+"'"+"Deportes"+"'"+",'"+"Fútbol Sala"+"',"+"0.1667)");
				db.execSQL("insert into Actividades(Tipo,Nombre,Valor) values("+"'"+"Deportes"+"'"+",'"+"Golf "+"',"+"0.1012)");
				db.execSQL("insert into Actividades(Tipo,Nombre,Valor) values("+"'"+"Deportes"+"'"+",'"+"Natación Moderada"+"',"+"0.0704)");
				db.execSQL("insert into Actividades(Tipo,Nombre,Valor) values("+"'"+"Deportes"+"'"+",'"+"Natación Vigorosa"+"',"+"0.1936)");
				db.execSQL("insert into Actividades(Tipo,Nombre,Valor) values("+"'"+"Deportes"+"'"+",'"+"Ping-pong (tenis de mesa)"+"',"+"0.099)");
				db.execSQL("insert into Actividades(Tipo,Nombre,Valor) values("+"'"+"Deportes"+"'"+",'"+"Trote lento"+"',"+"0.132)");
				db.execSQL("insert into Actividades(Tipo,Nombre,Valor) values("+"'"+"Deportes"+"'"+",'"+"Trote rápido"+"',"+"0.2024)");
				db.execSQL("insert into Actividades(Tipo,Nombre,Valor) values("+"'"+"Deportes"+"'"+",'"+"Carrera lenta"+"',"+"0.2288)");
				db.execSQL("insert into Actividades(Tipo,Nombre,Valor) values("+"'"+"Deportes"+"'"+",'"+"Carrera rápida"+"',"+"0.2838)");
				db.execSQL("insert into Actividades(Tipo,Nombre,Valor) values("+"'"+"Deportes"+"'"+",'"+"Vóleybol"+"',"+"0.143)");
				db.execSQL("insert into Actividades(Tipo,Nombre,Valor) values("+"'"+"Actividades Diarias"+"'"+",'"+"Andar con un Bebe en Brazos"+"',"+"0.033)");
				db.execSQL("insert into Actividades(Tipo,Nombre,Valor) values("+"'"+"Actividades Diarias"+"'"+",'"+"Cocinar"+"',"+"0.0166)");
				db.execSQL("insert into Actividades(Tipo,Nombre,Valor) values("+"'"+"Actividades Diarias"+"'"+",'"+"Cuidado de Niños (Esfuerzo bajo)"+"',"+"0.030)");
				db.execSQL("insert into Actividades(Tipo,Nombre,Valor) values("+"'"+"Actividades Diarias"+"'"+",'"+"Cuidado de Niños (Esfuerzo medio)"+"',"+"0.05)");
				db.execSQL("insert into Actividades(Tipo,Nombre,Valor) values("+"'"+"Actividades Diarias"+"'"+",'"+"Cuidado de Niños (Esfuerzo alto)"+"',"+"0.066)");
				db.execSQL("insert into Actividades(Tipo,Nombre,Valor) values("+"'"+"Actividades Diarias"+"'"+",'"+"Dormir"+"',"+"0.00033)");
				db.execSQL("insert into Actividades(Tipo,Nombre,Valor) values("+"'"+"Actividades Diarias"+"'"+",'"+"Estudiar"+"',"+"0.00333)");
				db.execSQL("insert into Actividades(Tipo,Nombre,Valor) values("+"'"+"Actividades Diarias"+"'"+",'"+"Regar las Plantas"+"',"+"0.0253)");
				db.execSQL("insert into Actividades(Tipo,Nombre,Valor) values("+"'"+"Actividades Diarias"+"'"+",'"+"Sin Actividad"+"',"+"0.000166)");
				db.execSQL("insert into Actividades(Tipo,Nombre,Valor) values("+"'"+"Actividades Diarias"+"'"+",'"+"Uso de Equipos Automatizados"+"',"+"0.025)");
				db.execSQL("insert into Actividades(Tipo,Nombre,Valor) values("+"'"+"Actividades Diarias"+"'"+",'"+"Ver la Telivisión"+"',"+"0.00166)");
				db.setTransactionSuccessful();
			}
			finally
			{
				db.endTransaction();
			}
				System.out.println("holaaaaaaaa");
			
		
		
		
		}

		@Override
		public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
			// TODO Auto-generated method stub
			
		}
		public List<Control> getControl()//para poder obtener toda las base de datos de los clientes
		{
			List<Control> lista=new ArrayList<Control>();
			String consulta="select Valor,Fecha,Id_Ac from Control";
			String consulta2="";
			SQLiteDatabase db=this.getWritableDatabase();
			Cursor cur=db.rawQuery(consulta, null);
			String a="",b="";
			if(cur.moveToFirst())
			{
				do
				{
					float d=Float.parseFloat(cur.getString(0));
					String e=cur.getString(1);
					String x=cur.getString(2);
					consulta2="select Tipo,Nombre from Actividades where Id_Ac="+x;
					Cursor cur2=db.rawQuery(consulta2, null);
					if(cur2.moveToFirst())
					{
						a=cur2.getString(0);
						b=cur2.getString(1);
					}
					Control c=new Control(a,b,d,e);
					lista.add(c);
				}while(cur.moveToNext());
			}
			return lista;
		}
		public ArrayList<String> getControlString()
		{
			List<Control> lista=getControl();
			ArrayList<String> res=new ArrayList<String>();
			for (int i = 0; i<lista.size(); i++) 
			{
				res.add(""+(i+1)+".-"+"\n"+"Tipo de Actividad: "+lista.get(i).getTipo()+" -> "+lista.get(i).getNombre()+"\n"+"Calorias Quemadas: "+lista.get(i).getValor()+" Kcal"+"\n"+"Fecha: "+lista.get(i).getFecha());
			}
			return res;
		}
	}

