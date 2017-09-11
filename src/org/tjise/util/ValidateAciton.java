package org.tjise.util;

import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import org.apache.struts2.ServletActionContext;
import org.tjise.crawler.Operation;
import org.tjise.crawler.Website;

import com.opensymphony.xwork2.ActionSupport;

public class ValidateAciton extends ActionSupport {

	/**
	 * 
	 */
	private static final long serialVersionUID = -2501304847481056251L;
	
	private Website website;
	private List<Website> webs;
	
	
	public List<Website> getWebs() {
		return webs;
	}

	public void setWebs(List<Website> webs) {
		this.webs = webs;
	}

	public Website getWebsite() {
		return website;
	}

	public void setWebsite(Website website) {
		this.website = website;
	}

	public String execute(){
		
			Operation op = new Operation();
			op.add(website);
		
			return "success";
		
	}
	
	public void validateExecute() {
		
		String regex = "[\u0391-\uFFE5]+$|[A-Za-z][A-Za-z1-9_-]+$";
		Pattern pattern = Pattern.compile(regex, Pattern.CASE_INSENSITIVE);
		Matcher matcher = pattern.matcher(website.getName());
		System.out.println(website.getName().length());
		System.out.println(matcher.matches());
		
		if(website.getName().length()>32 && website.getName().length()<4){
        	super.addFieldError("len", "网站名字需要在4到32个字符之间！");
            
        	return;
        }else if(website.getName() == null || "".equals(website.getName().trim())){
            super.addFieldError("notnull", "网站名字不能为空！");
            return;
        }
        if(!matcher.matches()){
        	super.addFieldError("test", "网站名字的字符非法");
            return;
        }
        
        
        if(website.getChannel()==null || "".equals(website.getChannel().trim())){
            super.addFieldError("url", "网站地址能为空！");
            return;
        }
        if(!matcher.matches()){
        	super.addFieldError("test", "网站地址有无效字符");
            return;
        }
        
        if(website.getTitle()==null || "".equals(website.getTitle().trim())
        		&& website.getAuthor()==null || "".equals(website.getAuthor().trim())
        		&& website.getPubtime()==null || "".equals(website.getPubtime().trim())
        		&& website.getContent()==null || "".equals(website.getContent().trim())
        		&& website.getSource()==null || "".equals(website.getSource().trim())){
            super.addFieldError("path", "Xpath不能为空");
            return;
        }
    }
	
	public String execute2(){
		Operation op = new Operation();
		webs = op.Allselect();
		
		return "success";
		
	}
	
	public String execute3(){
		Operation op = new Operation();
		op.delete(website.getName());
		webs = op.Allselect();
		return "success";
		
	}
	
	public void validateExecute3() {
		
		if(website.getName()==null || "".equals(website.getName().trim())){
            super.addFieldError("url", "网站名字不能为空！");
            return;
        }

		
		if(website.getChannel()==null || "".equals(website.getChannel().trim())){
            super.addFieldError("url", "网站地址不能为空！");
            return;
        }
		
		
	}
	
	public String execute4(){
		Operation op = new Operation();
		op.update(website.getName(),website.getChannel());
		webs = op.Allselect();
		return "success";
		
	}
	
	public String execute5(){
		Operation op = new Operation();
		op.Allupdate(String.valueOf(website.getId()),website);
		webs = op.Allselect();
		return "success";
		
	}
	
public void validateExecute4() {
		
	if(website.getName()==null || "".equals(website.getName().trim())){
        super.addFieldError("url", "网站名字不能为空！");
        return;
    }
	}
	
	public String quit(){
		
		return "input";
		
	}
	

}
