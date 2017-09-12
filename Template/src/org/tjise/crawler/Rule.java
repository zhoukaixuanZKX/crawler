package org.tjise.crawler;

public class Rule {
	private int id;
	private String url;					//连接
	private String[] params;			//参数集合
	private String[] values;			//参数对应值
	private String resultTagName;		//对返回的HTML，第一次过滤所用的标签，请先设置type
	private int type = ID;				//CLASS/ID/SELECTION 设置resultTagName的类型，默认为ID
	private int requestMoethod = GET;	//GET/POST 请求的类型，默认GET
	
	public final static int GET = 0 ;  
    public final static int POST = 1 ;  

    public final static int CLASS = 0;  
    public final static int ID = 1;  
    public final static int SELECTION = 2;
	
    
    public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public String getUrl() {
		return url;
	}
	public void setUrl(String url) {
		this.url = url;
	}
	public String[] getParams() {
		return params;
	}
	public void setParams(String[] params) {
		this.params = params;
	}
	public String[] getValues() {
		return values;
	}
	public void setValues(String[] values) {
		this.values = values;
	}
	public String getResultTagName() {
		return resultTagName;
	}
	public void setResultTagName(String resultTagName) {
		this.resultTagName = resultTagName;
	}
	public int getType() {
		return type;
	}
	public void setType(int type) {
		this.type = type;
	}
	public int getRequestMoethod() {
		return requestMoethod;
	}
	public void setRequestMoethod(int requestMoethod) {
		this.requestMoethod = requestMoethod;
	} 
	
}
