package com.example.fitweb;

import java.util.ArrayList;



import android.app.Activity;
import android.database.sqlite.SQLiteDatabase;
import android.os.Bundle;
import android.widget.ArrayAdapter;
import android.widget.ListView;

public class Informacion_Cal extends Activity
{
	//ArrayList<String> NombreActividad=new ArrayList<String>();
	//ArrayList<String> Cal=new ArrayList<String>();
	private ListView lis;
	@Override
	protected void onCreate(Bundle savedInstanceState)
	{
		super.onCreate(savedInstanceState);
		setContentView(R.layout.informacion);
		//SQLiteDatabase db=MainActivity.base;
		lis=(ListView) findViewById(R.id.ListaControl);
		//db.rawQuery(sql, selectionArgs)
		DbHelper db=new DbHelper(this);
		ArrayAdapter<String> adapter=new ArrayAdapter<String>
		(this, R.layout.listaletras,db.getControlString());
		lis.setAdapter(adapter);
	}
}
