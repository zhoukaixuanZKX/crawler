package org.tjise.crawler;

import java.io.UnsupportedEncodingException;
import java.sql.Time;



public class Website {
	private int id;
	private String name; //站点名字
	private String channel; //频道信息
	private String region;  //境内外
	private String contry;  //国家名字
	private String language; //语种
	
	
	private Time start_time; //开始时间
	private Time stop_time; //结束时间
	
	private String title; //文章标题的path
	private String author; //文章作者的path
	private String pubtime; //发布时间的path
	private String content; //正文的path
	private String source; //转发来源的path
	private String Disable = "false";
	
	public String getDisable() {
		return Disable;
	}
	public void setDisable(String disable) {
		Disable = disable;
	}
	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public String getName() {
		
		return name;
	}
	public void setName(String name) throws UnsupportedEncodingException {
		//String name2 = new String(name.getBytes(),"utf-8");
		this.name = name;
	}
	public String getChannel() {
		return channel;
	}
	public void setChannel(String channel) {
		this.channel = channel;
	}
	public Time getStart_time() {
		return start_time;
	}
	public void setStart_time(Time start_time) {
		this.start_time = start_time;
	}
	public Time getStop_time() {
		return stop_time;
	}
	public void setStop_time(Time stop_time) {
		this.stop_time = stop_time;
	}
	public String getTitle() {
		return title;
	}
	public void setTitle(String title) {
		this.title = title;
	}
	public String getAuthor() {
		return author;
	}
	public void setAuthor(String author) {
		this.author = author;
	}
	public String getPubtime() {
		return pubtime;
	}
	public void setPubtime(String pubtime) {
		this.pubtime = pubtime;
	}
	public String getContent() {
		return content;
	}
	public void setContent(String content) {
		this.content = content;
	}
	public String getSource() {
		return source;
	}
	public void setSource(String source) {
		this.source = source;
	}
	
	
	public String getRegion() {
		return region;
	}
	public void setRegion(String region) {
		this.region = region;
	}
	public String getContry() {
		return contry;
	}
	public void setContry(String contry) {
		this.contry = contry;
	}
	public String getLanguage() {
		return language;
	}
	public void setLanguage(String language) {
		this.language = language;
	}
	@Override
	public String toString() {
		return "Website [id=" + id + ", name=" + name + ", channel=" + channel
				+ ", region=" + region + ", contry=" + contry + ", language="
				+ language + ", start_time=" + start_time + ", stop_time="
				+ stop_time + ", title=" + title + ", author=" + author
				+ ", pubtime=" + pubtime + ", content=" + content + ", source="
				+ source + "]";
	}
	
	
}
