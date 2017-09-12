package org.tjise.Contact;

import java.io.BufferedReader;
import java.io.InputStreamReader;

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
	                
	                System.out.println(line);
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
				
				System.out.println(line);
			}
			
			in.close();
			pr.waitFor();
			
		} catch (Exception e) {
			e.printStackTrace();
		}
		System.out.println("end");
		
	}
}
