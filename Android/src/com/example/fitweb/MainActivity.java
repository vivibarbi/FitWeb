package com.example.fitweb;



import android.R.layout;
import android.os.Bundle;
import android.app.Activity;
import android.content.Intent;
import android.database.sqlite.SQLiteDatabase;
import android.view.Menu;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.RelativeLayout;
import android.widget.TextView;
import android.widget.AdapterView.OnItemClickListener;
import android.view.*;
import android.graphics.Color;
public class MainActivity extends Activity {
	
	private String[] paises={"Informacion","Maquinas","Deportes","Actividades Diarias"};
	//private String[] habitantes={"40000000","17000000","11000000"};
	private TextView tv1;
	private ListView lv1;
	private RelativeLayout lay;
	static String aux="";
	static SQLiteDatabase base;
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
		DbHelper helper=new DbHelper(this);
		base=helper.getWritableDatabase();
		lay=(RelativeLayout) findViewById(R.id.RelativeLayout1);
		//lay.setBackgroundColor(Color.GREEN);
		//tv1=(TextView) findViewById(R.id.tv1);
		lv1=(ListView) findViewById(R.id.listView1);
		ArrayAdapter<String> adapter=new ArrayAdapter<String>(this,R.layout.listaletras, paises);
		lv1.setAdapter(adapter);
		//lv1.setBackgroundColor(0xff299230);
		
		lv1.setOnItemClickListener(new OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View v, int posicion, long id) {
                //tv1.setText("Población de "+ lv1.getItemAtPosition(posicion) + " es "+ habitantes[posicion]);
            	aux=lv1.getItemAtPosition(posicion)+"";
            	System.out.println(aux);
            	if(aux.compareTo("Deportes")==0||aux.compareTo("Actividades Diarias")==0)
            	{
	            	Intent intent =
	                        new Intent(MainActivity.this, MenuDeportes.class);
	
	                //Creamos la información a pasar entre actividades
	                //Bundle b = new Bundle();
	                //b.putString("NOMBRE", txtNombre.getText().toString());
	
	                //Añadimos la información al intent
	                //intent.putExtras(b);
	
	                //Iniciamos la nueva actividad
	                
	                startActivity(intent);
	            }
            	else
            	{
	            	if(aux.compareTo("Informacion")==0)
	            	{
	            		Intent intent=
	            				new Intent(MainActivity.this, Informacion_Cal.class);
	            		startActivity(intent);
	            	}
            	}
            }
        });	
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.main, menu);
		return true;
	}

}
