<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib uri="/struts-tags" prefix="s" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %> 
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Success Page</title>
</head>
<body>
    <h1>现有信息:</h1> <br/>
 		<s:form action="register3" method="post">
    	 <s:textfield label="站点名字" name="website.name" tooltip="站点名字 如：百度"></s:textfield>
    	 <s:textfield label="频道地址" name="website.channel" tooltip="频道的url地址"></s:textfield>
    	<s:submit label="Register"   value="删除" />
    	<s:submit label="Register"  action="register4"  value="修改" />
    	<s:submit label="Register"  action="quit"  value="返回" />
    	</s:form>
    	
    <c:forEach items="${webs}" var="list">
    	
    	<pre>${list.name}:  ${list.channel} 
    	</pre>
    	
    
    </c:forEach>

</body>
</html>