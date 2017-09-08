package org.tjise.crawler;

import java.util.HashSet;
import java.util.Set;

import org.hibernate.Query;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;



public class Tset {

	public static void main(String[] args) {
		Operation op = new Operation();
		//op.delete("百度");
		op.delete("谷歌");
	}

}
