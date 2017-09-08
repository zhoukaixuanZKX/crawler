package org.tjise.crawler;

import java.sql.Time;



public class Website {
	private int id;
	private String name; //站点名字
	private String channel; //频道信息
	
	private Time start_time; //开始时间
	private Time stop_time; //结束时间
	
	private String title; //文章标题的xpath
	private String author; //文章作者的xpath
	private String pubtime; //发布时间的xpath
	private String content; //正文的xpath
	private String source; //转发来源的xpath
	
	
	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
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
	
	
	@Override
	public String toString() {
		return "Website [id=" + id + ", name=" + name + ", channel=" + channel
				+ ", start_time=" + start_time + ", stop_time=" + stop_time
				+ ", title=" + title + ", author=" + author + ", pubtime="
				+ pubtime + ", content=" + content + ", source=" + source + "]";
	}
	
	
	
}
