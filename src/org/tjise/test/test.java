package org.tjise.test;


import javassist.tools.web.Webserver;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;
import org.tjise.crawler.LinkTypeData;
import org.tjise.crawler.Operation;
import org.tjise.crawler.Rule;
import org.tjise.crawler.Website;



public class test {

	public static void main(String[] args) {
		// 获取 Hibernate配置信息
				Configuration configuration = new Configuration().configure();
				// 根据 configuration建立sessionFactory
				SessionFactory sessionFactory = configuration.buildSessionFactory();
				// 开启 session（相当于开启JDBC的connection）
				Session session = sessionFactory.openSession();
				//创建并开启事务对象
				session.beginTransaction();
				
				LinkTypeData ltd = new LinkTypeData();
				ltd.setId(2);
				
				session.save(ltd);
				
				//事务提交
				session.getTransaction().commit();
				//关闭session和sessionFactory
				session.close();
				sessionFactory.close();

	}

}
