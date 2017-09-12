package org.tjise.crawler;



public class LinkTypeData {
	private int id; 
	private String linkHref; //连接
	private String linkText; //名字
	private String uploadr; //摘要
	private String read; //内容
	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public String getLinkHref() {
		return linkHref;
	}
	public void setLinkHref(String linkHref) {
		this.linkHref = linkHref;
	}
	public String getLinkText() {
		return linkText;
	}
	public void setLinkText(String linkText) {
		this.linkText = linkText;
	}
	public String getUploadr() {
		return uploadr;
	}
	public void setUploadr(String uploadr) {
		this.uploadr = uploadr;
	}
	public String getRead() {
		return read;
	}
	public void setRead(String read) {
		this.read = read;
	}
	
	
}
