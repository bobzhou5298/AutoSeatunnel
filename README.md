# AutoSeatunnel
背景：因有时候需要自动化批量抽取和导出MySQL数据，落地到本地路径或S3库，开始接触Seatunnel，发现可以满足需求，为了提高开发效率，希望能读取MySQL元数据后自动生成Seatunnel的配置文件，故产生了用python去自动化生成想法，这就是这个项目的来源初衷。目前只写了满足我需求的几个Connector,如果你刚好需要可自取，如果你有更好的想法，欢迎补充，谢谢。

目录结构说明
  Config : 自定义类Seatunnel,Env,Source,Sink,Transform及各个属性
  Connector ：连接器Connector
    Source：定义数据来源类JDBC,Hive,Kafka,S3File等，后续补充其他的Connector
    Sink： 定义数据落地类Console,Email,LocalFile等，后续补充其他的Connector
  Data： 自定义配置文件和生成的配置文件数据存放路径
  Docs：操作文档，暂无
  Env： 自定义Seatunnel类ENV
  Transform: 自定义Seatunnel类Transform
  Uage: 各类用法说明
  Util：工具类存放路径，目前只有读取MySQL的元数据生成配置文件的方法

  
