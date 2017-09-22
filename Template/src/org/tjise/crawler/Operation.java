package org.tjise.crawler;



import java.io.UnsupportedEncodingException;
import java.util.List;

import org.hibernate.Query;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;


public class Operation {
	/**
	 * 获取sessionFactory
	 * @return
	 */
	private static SessionFactory getsessionFactory(){
		// 获取 Hibernate配置信息
		Configuration configuration = new Configuration().configure();
		// 根据 configuration建立sessionFactory
		return configuration.buildSessionFactory();
	}
	/**
	 *获取session
	 * @param sessionFactory
	 * @return
	 */
	private static Session Connection(SessionFactory sessionFactory) {
		
		// 开启 session（相当于开启JDBC的connection）
		Session session = sessionFactory.openSession();
		//创建并开启事务对象
		session.beginTransaction();
		
		
		return session;
	}
	/**
	 * 添加多个website
	 * @param webs
	 */
	public void add(List<Website> webs){
		//新建对象，并赋值
		SessionFactory sessionFactory = getsessionFactory();
		Session session = Connection(sessionFactory);
		Website user = new Website();
		
		//保存对象
		for(Website web : webs){
			session.save(web);
		}
		//事务提交
		session.getTransaction().commit();
		//关闭session和sessionFactory
		session.close();
		sessionFactory.close();
	}
	/**
	 * 添加单个website
	 * @param web
	 */
	public void add(Website web){
		//新建对象，并赋值
		SessionFactory sessionFactory = getsessionFactory();
		Session session = Connection(sessionFactory);
		Website user = new Website();
		
		//保存对象
		
		session.save(web);
		
		//事务提交
		session.getTransaction().commit();
		//关闭session和sessionFactory
		session.close();
		sessionFactory.close();
	}
	/**
	 * 查询所有数据
	 */
	public List<Website> Allselect(boolean flage){
		SessionFactory sessionFactory = getsessionFactory();
		Session session = Connection(sessionFactory);
		//利用stringbuilder来连接查询语句
		StringBuilder hq = new StringBuilder();
		//从user里面查找（注意from后有空格）
		//相当于“selset * from user_info；”
		hq.append("from ").append(Website.class.getName());
		if(flage){
			hq.append(" where region = 'false'");
		}
		//利用 session 建立 query
		Query query = session.createQuery(hq.toString());
		//序列化query的结果为一个list集合
		List<Website> webs = query.list();
		//打印每一个user信息（这里只打印了名字，你也可以打印其他信息）
		
		/*for(Website web :webs){
			System.out.println(web.toString());
			
		}*/
		
		session.getTransaction().commit();
		session.clear();
		sessionFactory.close();
		
		
		return webs;
	}
	
	/**
	 * 查询ID对应的数据
	 */
	public List<Website> IDselect(String id){
		SessionFactory sessionFactory = getsessionFactory();
		Session session = Connection(sessionFactory);
		//利用stringbuilder来连接查询语句
		StringBuilder hq = new StringBuilder();
		//从user里面查找（注意from后有空格）
		//相当于“selset * from user_info；”
		hq.append("from ").append(Website.class.getName())
							.append(" where id =:id");
		//利用 session 建立 query
		Query query = session.createQuery(hq.toString());
		query.setString("id", id);
		System.out.println(Website.class.getName());
		//序列化query的结果为一个list集合
		List<Website> webs = query.list();
		//打印每一个user信息（这里只打印了名字，你也可以打印其他信息）
		
		session.getTransaction().commit();
		session.clear();
		sessionFactory.close();
		
		
		return webs;
	}
	
	/**
	 * 修改数据
	 * @param name
	 * @param channel
	 */
	public void update(String id,String channel){
		SessionFactory sessionFactory = getsessionFactory();
		Session session = Connection(sessionFactory);
		StringBuilder hq = new StringBuilder();
		//对比查找的操作来看，因为无门需要修改指定name的用户密码，后面需要再添加查询条件
		//注意 from 、 where 的空格，“：name” 表示一个参数
		hq.append("from ").append(Website.class.getName())
		  .append(" where id=:id");
		Query query = session.createQuery(hq.toString());
		//这里就设定参数name的值为“user1”
		query.setString("id", id);
		System.out.println(hq);
		List<Website> webs = query.list();
		for(Website web : webs){
			//修改user1的密码
			web.setChannel(channel);
			//注意这里是update
			session.update(web);
		}
		session.getTransaction().commit();
		session.clear();
		sessionFactory.close();
	}
	
	/**
	 * 修改数据
	 * @param name
	 * @param channel
	 * @throws UnsupportedEncodingException 
	 */
	public void Allupdate(String id,Website nweb) throws UnsupportedEncodingException{
		SessionFactory sessionFactory = getsessionFactory();
		Session session = Connection(sessionFactory);
		StringBuilder hq = new StringBuilder();
		//对比查找的操作来看，因为无门需要修改指定name的用户密码，后面需要再添加查询条件
		//注意 from 、 where 的空格，“：name” 表示一个参数
		hq.append("from ").append(Website.class.getName())
		  .append(" where id=:id");
		Query query = session.createQuery(hq.toString());
		//这里就设定参数name的值为“user1”
		query.setString("id", id);
		List<Website> webs = query.list();
		
		System.out.println(hq);
		System.out.println(nweb);
		System.out.println(webs);
		
		for(Website web : webs){
			if(nweb.getChannel() != null && !"".equals(nweb.getChannel().trim()))
				{web.setChannel(nweb.getChannel());}
			if(nweb.getContent() != null && !"".equals(nweb.getContent().trim()))
				{web.setContent(nweb.getContent());}
			if(nweb.getAuthor() != null && !"".equals(nweb.getAuthor().trim()))
				{web.setAuthor(nweb.getAuthor());}
			if(nweb.getName() != null && !"".equals(nweb.getName().trim()))
				{web.setName(nweb.getName());}
			if(nweb.getContry() != null && !"".equals(nweb.getContry().trim()))
				{web.setContry(nweb.getContry());}
			if(nweb.getLanguage() != null && !"".equals(nweb.getLanguage().trim()))
			 	{web.setLanguage(nweb.getLanguage());}
			if(nweb.getTitle() != null && !"".equals(nweb.getTitle().trim()))
				{web.setTitle(nweb.getTitle());}
			if(nweb.getPubtime() != null && !"".equals(nweb.getPubtime().trim()))
				{web.setPubtime(nweb.getPubtime());}
			if(nweb.getRegion() != null && !"".equals(nweb.getRegion().trim()))
				{web.setRegion(nweb.getRegion());}
			if(nweb.getSource() != null && !"".equals(nweb.getSource().trim()))
				{web.setSource(nweb.getSource());}
			if(nweb.getDisable() != null && !"".equals(nweb.getDisable().trim()))
				{web.setDisable(nweb.getDisable());}
			
			//注意这里是update
			session.update(web);
		}
		session.getTransaction().commit();
		session.clear();
		sessionFactory.close();
	}
	
	/**
	 * 删除数据
	 * @param name
	 */
	public void delete(String name){
		SessionFactory sessionFactory = getsessionFactory();
		Session session = Connection(sessionFactory);
		StringBuilder hq = new StringBuilder();
		//对比查找时候的操作来看，需要修改指定name的网址，后面需要再添加查询条件
		hq.append("from ").append(Website.class.getName())
		  .append(" where name=:name");
		Query query = session.createQuery(hq.toString());
		query.setString("name", name);
		List<Website> webs = query.list();
		for(Website web :webs){
			session.delete(web);
		}
		
		session.getTransaction().commit();
		session.clear();
		sessionFactory.close();
	}
	
	
}
