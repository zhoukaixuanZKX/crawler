<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib uri="/struts-tags" prefix="s" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Insert title here</title>
</head>
<body>
<h2>模板录入</h2>

    <s:fielderror />
    <s:form action="register" method="post">   
        <s:textfield label="站点名字" name="website.name" tooltip="站点名字 如：百度"></s:textfield>
        <s:textfield label="频道地址" name="website.channel" tooltip="频道的url地址"></s:textfield>
        <!-- 
        <s:textfield label="start_time" name="website.start_time"></s:textfield>
        <s:textfield label="stop_time" name="website.stop_time" tooltip="age must over 16"></s:textfield>
         -->
        <s:textfield label="文章标题的xpath" name="website.title" tooltip="标签"></s:textfield>
        <s:textfield label="文章作者的xpath" name="website.author" tooltip="标签"></s:textfield>
        <s:textfield label="发布时间的xpath" name="website.pubtime" tooltip="i标签"></s:textfield>
        <s:textfield label="正文的xpath" name="website.content" tooltip="标签"></s:textfield>
        <s:textfield label="转发来源的xpath" name="website.source" tooltip="标签"></s:textfield>

        <s:submit label="Register" value="录入"></s:submit>  
   		<s:submit label="Register" action="register2"  value="查看" ></s:submit>  
 	</s:form>
 	
 	
</body>
</html>