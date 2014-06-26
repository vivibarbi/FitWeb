package com.example.fitweb;



import android.app.Activity;
import android.content.Intent;
import android.graphics.Color;
import android.os.Bundle;
import android.text.Layout;
import android.view.Menu;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.LinearLayout;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.AdapterView.OnItemClickListener;

public class MenuDeportes extends Activity {
	private String[] deportes={"Básquetbol Moderado","Básquetbol Vigoroso","Bicicleta Vel. Baja","Bicicleta Vel. Moderada","Boxeo Moderado","Boxeo Vigoroso","Caminata Moderada","Caminata Vigorosa","Fútbol Moderado","Fútbol Vigoroso","Fútbol Sala","Golf","Natación Moderada","Natación Vigorosa","Ping-pong (tenis de mesa)","Trote lento","Trote rápido","Carrera lenta","Carrera rápida","Vóleybol"};
	private String[] actividad={"Andar con un Bebe en Brazos","Cocinar","Cuidado de Niños (Esfuerzo bajo)","Cuidado de Niños (Esfuerzo medio)","Cuidado de Niños (Esfuerzo alto)","Dormir","Estudiar","Regar las Plantas","Sin Actividad","Uso de Equipos Automatizados","Ver la Telivisión"};
	private String[] TipoAct;
	private ListView Medepor;
	private LinearLayout lin;
	static String aux_nom;
	@Override
	protected void onCreate(Bundle savedInstanceState)
	{
		super.onCreate(savedInstanceState);
		setContentView(R.layout.fitweb_deportes);
		//lin=(LinearLayout) findViewById(R.id.VenDep);
		//lin.setBackgroundColor(Color.GREEN);
		String activi=MainActivity.aux;
		Medepor=(ListView) findViewById(R.id.DeportesMenu);
		if(activi.compareTo("Deportes")==0)
		{
			TipoAct=deportes;
		}
		if(activi.compareTo("Actividades Diarias")==0)
		{
			TipoAct=actividad;
		}
		ArrayAdapter<String> adapter=new ArrayAdapter<String>(this,R.layout.listaletras, TipoAct);
		Medepor.setAdapter(adapter);
	
		Medepor.setOnItemClickListener(new OnItemClickListener()  {
			@Override
			public void onItemClick(AdapterView<?> parent, View v, int posicion, long id) {
				
				aux_nom=Medepor.getItemAtPosition(posicion)+"";
				Intent intent =
                        new Intent(MenuDeportes.this, Control_cal.class);
                startActivity(intent);
				
			}
			
			
		});
		
	}



}
