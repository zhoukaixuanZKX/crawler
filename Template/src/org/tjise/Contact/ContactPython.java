package org.tjise.Contact;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.List;

import org.tjise.crawler.Website;

public class ContactPython {
	
	private static final String PY = "python";
	
	public void StaticContact(String path) {
		System.out.println("start");
		String[] arg = new String[] {PY,path};
		 try {
	            Process pr = Runtime.getRuntime().exec(arg);
	            BufferedReader in = new BufferedReader(new InputStreamReader(pr.getInputStream()));
	            String line;
	            while ((line = in.readLine()) != null) {
	            	String lines = new String(line.getBytes("utf-8"),"utf-8");
					System.out.println(lines);
					
	            }
	            
	            in.close();
	            pr.waitFor();
	           
	        } catch (Exception e) {
	            e.printStackTrace();
	        }
		 System.out.println("end");
		
	}
	public void DynamocContact(String path,Website web) {
		System.out.println("start");
		String[] arg = new String[] {PY,path,web.toString()};
		try {
			Process pr = Runtime.getRuntime().exec(arg);
			BufferedReader in = new BufferedReader(new InputStreamReader(pr.getInputStream()));
			String line;

			while ((line = in.readLine()) != null) {
				String lines = new String(line.getBytes("UTF-8"),"GBK");
				System.out.println(lines);
				
			}
			
			in.close();
			pr.waitFor();
			
		} catch (Exception e) {
			e.printStackTrace();
		}
		System.out.println("end");
		
	}
}
