package com.example.fitweb;





import java.util.Timer;
import java.util.TimerTask;

import android.app.Activity;
import android.app.AlertDialog;
import android.media.MediaPlayer;
import android.os.Bundle;
import android.os.SystemClock;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.Chronometer;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;
import android.content.Intent;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.view.LayoutInflater;;
public class Control_cal extends Activity {
	
	Chronometer cronometro;
	Long memoCronometro;
	String contnue="inactive";
	String tipo=MainActivity.aux;
	String nombre=MenuDeportes.aux_nom;
	Button btnStart;
	Button btnStop;
	EditText peso;
	MediaPlayer mp;
	AlertDialog.Builder dialogo1;
	float val;
	int con=0;
	@Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.control_calorias);
      /*  DbHelper data=new DbHelper(this);
       final SQLiteDatabase db=data.getWritableDatabase();*/
        dialogo1 = new AlertDialog.Builder(this);
        dialogo1.setTitle("Total de Calorias Quemadas");
        cronometro=(Chronometer)findViewById(R.id.chronometer1);
        btnStart=(Button)findViewById(R.id.btn_star);
		btnStop=(Button)findViewById(R.id.btn_stop);
		peso=(EditText)findViewById(R.id.editText1);
		mp=MediaPlayer.create(this,R.raw.bip2);
		Timer timer=new Timer();
		timer.scheduleAtFixedRate(new TimerTask() {
			@Override
			public void run() {
				//La función que queremos ejecutar
				FuncionParaEsteHilo();
			}
		}, 0, 1300);
	}
	private void FuncionParaEsteHilo()
	{
	    //Esta función es llamada des de dentro del Timer
		//Para no provocar errores ejecutamos el Accion
		//Dentro del mismo Hilo
	    this.runOnUiThread(Accion);
	}
	private Runnable Accion = new Runnable() {
	    public void run() {
	    //Aquí iría lo que queramos que haga,
	    //en este caso mostrar un mensaje.
	    	//Toast.makeText(getApplicationContext(), "Tiempo!", Toast.LENGTH_LONG).show();
	    	if(con==1)
	    		mp.start();
	
		btnStart.setOnClickListener(new OnClickListener() {
			
			@Override
			
			public void onClick(View v) {
				
				
				if(contnue=="inactive")
				{
					cronometro.setBase(SystemClock.elapsedRealtime());
					cronometro.start();
					contnue="active";
					con=1;
					btnStart.setText("Pause");
					return;
				}
				if(contnue=="active")
				{
					memoCronometro=SystemClock.elapsedRealtime();
					cronometro.stop();
					contnue="pause";
					con=0;
					btnStart.setText("Coninuar");
					return;
				}
				if(contnue=="pause")
				{
					cronometro.setBase((long)cronometro.getBase()-memoCronometro+SystemClock.elapsedRealtime());
					cronometro.start();
					contnue="active";
					con=1;
					btnStart.setText("Pause");
				}
				
			}
		});
		
		btnStop.setOnClickListener(new OnClickListener() {
			
			@Override
			public void onClick(View v) {
				if((peso.getText()+"").compareTo("")!=0)
				{
					
				con=0;
				SQLiteDatabase db=MainActivity.base;
				Cursor c=db.rawQuery("select Valor,Id_Ac from Actividades where Tipo='"+tipo+"' and Nombre='"+nombre+"'", null);
				String ayu="";
				int id=0;
				if(c.moveToFirst())
				{
					ayu=c.getString(0);
					id=Integer.parseInt(c.getString(1));
				}
				else
					ayu="Error";
				val=Float.parseFloat(ayu);
				cronometro.stop();
				btnStart.setText("Iniciar");
				contnue="inactive";
				String time=cronometro.getText()+"";
				String topeso=peso.getText()+"";
				val=Float.parseFloat(Calculo(val,time,topeso));
				
				db.execSQL("insert into Control(Valor,Id_Ac) values("+val+","+id+")");
				//db.close();
				dialogo1.setMessage("El Total de Calorias quemadas es de: "+val+" Kcal");
				//dialogo1.setCancelable(false);
				dialogo1.show();
				/*Intent intent =
                        new Intent(Control_cal.this, Control_cal.class);
                startActivity(intent);*/
				}
			}
			
		});
	    }
		};
	//}
	static String Calculo(float x,String time,String topeso)
	{
		String min=time.substring(0,2);
		String seg=time.substring(3,5);
		float minseg=Float.parseFloat(seg)/60;
		float tomin=Float.parseFloat(min)+minseg;
		float peso=Float.parseFloat(topeso);
		float val=tomin*x*peso;
		String aux=val+"";
		int c=9;
		String enviar="";
		int i=0;
		while(c>0)
		{
			if(aux.charAt(i)=='.')
				c=2;
			enviar=enviar+aux.charAt(i);
			c--;
			i++;
		}
		
		return enviar;
	}
}
