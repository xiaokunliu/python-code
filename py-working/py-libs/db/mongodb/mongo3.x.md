##### Mongo查询
* 文档参考链接：https://docs.mongodb.com/manual/tutorial/query-documents/
* db为mongo的数据库
* users为db下的一个collection
* 使用java和python代码
* 版本是mongo3.6

##### 基本查询

```text
# 数据准备
db.inventory.insertMany([
   { item: "journal", qty: 25, size: { h: 14, w: 21, uom: "cm" }, status: "A" },
   { item: "notebook", qty: 50, size: { h: 8.5, w: 11, uom: "in" }, status: "A" },
   { item: "paper", qty: 100, size: { h: 8.5, w: 11, uom: "in" }, status: "D" },
   { item: "planner", qty: 75, size: { h: 22.85, w: 30, uom: "cm" }, status: "D" },
   { item: "postcard", qty: 45, size: { h: 10, w: 15.25, uom: "cm" }, status: "A" }
]);
```

> 查询所有

```text
db.inventory.find( {} ) == SELECT * FROM inventory
```

> 根据`=`条件查询,`select * from inventory where status = 'D'`

```text
# { <field1>: <value1>, ... }
db.inventory.find( { status: "D" } )   
```
 
> 根据条件操作符查询

```text
# db.users.find({f1: {operator: []}, ...})
# 操作符： https://docs.mongodb.com/manual/reference/operator/query/#query-selectors
 
db.inventory.find( { status: { $in: [ "A", "D" ] } } )  ==  SELECT * FROM inventory WHERE status in ("A", "D")
```

> 定义使用And的条件

```text
db.inventory.find( { status: "A", qty: { $lt: 30 } } )  ==  SELECT * FROM inventory WHERE status = "A" AND qty < 30
```

> 使用OR的条件

```text
db.inventory.find( { $or: [ { status: "A" }, { qty: { $lt: 30 } } ] } )  ==  SELECT * FROM inventory WHERE status = "A" OR qty < 30
```

> 使用And和Or的组合

```text
db.inventory.find( {
     status: "A",
     $or: [ { qty: { $lt: 30 } }, { item: /^p/ } ]
} )

SELECT * FROM inventory WHERE status = "A" AND ( qty < 30 OR item LIKE "p%")
```

##### 查询嵌套

```text
## 数据准备
db.inventory.insertMany( [
   { item: "journal", qty: 25, size: { h: 14, w: 21, uom: "cm" }, status: "A" },
   { item: "notebook", qty: 50, size: { h: 8.5, w: 11, uom: "in" }, status: "A" },
   { item: "paper", qty: 100, size: { h: 8.5, w: 11, uom: "in" }, status: "D" },
   { item: "planner", qty: 75, size: { h: 22.85, w: 30, uom: "cm" }, status: "D" },
   { item: "postcard", qty: 45, size: { h: 10, w: 15.25, uom: "cm" }, status: "A" }
]);
```

> 查询文档中size等于{ h: 14, w: 21, uom: "cm" }

```text
# size将精准匹配文档的数据值,包括字段的顺序
db.inventory.find( { size: { h: 14, w: 21, uom: "cm" } } )  # 可以查询到

db.inventory.find(  { size: { w: 21, h: 14, uom: "cm" } }  ) # 查不到
```

> 根据嵌套的字段进行查询,使用field.nestedField

* 查询文档的size.uom的值为in
```text
db.inventory.find( { "size.uom": "in" } )
```

* 使用查询过滤和操作符

```text
# { <field1>: { <operator1>: <value1> }, ... }
db.inventory.find( { "size.h": { $lt: 15 } } )
```

* 使用AND的查询条件

```text
db.inventory.find( { "size.h": { $lt: 15 }, "size.uom": "in", status: "D" } )
```

#### 查询数组

```text
# 数据准备
db.inventory.insertMany([
   { item: "journal", qty: 25, tags: ["blank", "red"], dim_cm: [ 14, 21 ] },
   { item: "notebook", qty: 50, tags: ["red", "blank"], dim_cm: [ 14, 21 ] },
   { item: "paper", qty: 100, tags: ["red", "blank", "plain"], dim_cm: [ 14, 21 ] },
   { item: "planner", qty: 75, tags: ["blank", "red"], dim_cm: [ 22.85, 30 ] },
   { item: "postcard", qty: 45, tags: ["blue"], dim_cm: [ 10, 15.25 ] }
]);
```

> 查询匹配tags字段为red和blank的数组数据(精准匹配)

```text
db.inventory.find( { tags: ["red", "blank"] } )
```

> 查询字段tags的数组数据包含red和blank

```text
db.inventory.find( { tags: { $all: ["red", "blank"] } } )
```

> 查询tags字段包含red的值

```text
db.inventory.find( { tags: "red" } )
```

> 使用操作符，查询dim_cm中至少一个字段值大于25

```text
db.inventory.find( { dim_cm: { $gt: 25 } } )
```

> 使用操作符，查询dim_cm中有一个是大于15，而有一个是小于20，也可以是同时满足大于15小于20的字段值

```text
db.inventory.find( { dim_cm: { $gt: 15, $lt: 20 } } )
```

> 使用操作符，查询dim_cm中至少有一个是大于15并且小于20的两个条件

```text
db.inventory.find( { dim_cm: { $elemMatch: { $gt: 22, $lt: 30 } } } )
```

> 查询dim_cm数组中第二个元素大于20

```text
db.inventory.find( { "dim_cm.1": { $gt: 25 } } )
```

> 使用操作符,查询dim_cm数组元素个数大于3

```text
db.inventory.find( { "tags": { $size: 3 } } )
```

#### 查询嵌入式文档数组

```text
## 准备数据
db.inventory.insertMany( [
   { item: "journal", instock: [ { warehouse: "A", qty: 5 }, { warehouse: "C", qty: 15 } ] },
   { item: "notebook", instock: [ { warehouse: "C", qty: 5 } ] },
   { item: "paper", instock: [ { warehouse: "A", qty: 60 }, { warehouse: "B", qty: 15 } ] },
   { item: "planner", instock: [ { warehouse: "A", qty: 40 }, { warehouse: "B", qty: 5 } ] },
   { item: "postcard", instock: [ { warehouse: "B", qty: 15 }, { warehouse: "C", qty: 35 } ] }
]);
```

> 查询一个嵌套在数组中的文档

* 查询instock的数组中包含指定的文档{ warehouse: "A", qty: 5 }，属于精准匹配
```text
db.inventory.find( { "instock": { warehouse: "A", qty: 5 } } )
```

* 如果使用以下的查询,将查询不到结果数据
```text
db.inventory.find( { "instock": { qty: 5, warehouse: "A" } } )
```

* 查询instock数组中的文档至少包含一个qty<=20的数据
```text
db.inventory.find( { 'instock.qty': { $lte: 20 } } )
```

* 查询instock文档中至少有一个嵌入的文档包含{ qty: 5, warehouse: "A" }
```text
db.inventory.find( { "instock": { $elemMatch: { qty: 5, warehouse: "A" } } } )
```

* 查询instock数组嵌套的文档中包含qty的字段且小于10大于20
```text
db.inventory.find( { "instock.qty": { $gt: 10,  $lte: 20 } } )
```

* 查询instock数组嵌套的文档中至少有一个文档A包含qty字段值为5,并且至少(可以是文档A)文档B包字段值warehouse为A的数据
```text
db.inventory.find( { "instock.qty": 5, "instock.warehouse": "A" } )
```

##### 从query查询中查找指定的字段

```text
## 数据准备
db.inventory.insertMany( [
  { item: "journal", status: "A", size: { h: 14, w: 21, uom: "cm" }, instock: [ { warehouse: "A", qty: 5 } ] },
  { item: "notebook", status: "A",  size: { h: 8.5, w: 11, uom: "in" }, instock: [ { warehouse: "C", qty: 5 } ] },
  { item: "paper", status: "D", size: { h: 8.5, w: 11, uom: "in" }, instock: [ { warehouse: "A", qty: 60 } ] },
  { item: "planner", status: "D", size: { h: 22.85, w: 30, uom: "cm" }, instock: [ { warehouse: "A", qty: 40 } ] },
  { item: "postcard", status: "A", size: { h: 10, w: 15.25, uom: "cm" }, instock: [ { warehouse: "B", qty: 15 }, { warehouse: "C", qty: 35 } ] }
]);
```

> 查询所有的字段

```text
db.inventory.find( { status: "A" } )
```

> 仅查询指定的字段,item,status

```text
db.inventory.find( { status: "A" }, { item: 1, status: 1 } )  # 这时候是有_id查询出来
```

> 仅查询指定的字段,item,status,去掉_id

```text
db.inventory.find( { status: "A" }, { item: 1, status: 1, _id: 0 } )
```

> 返回所有字段但不包括的字段status和instock

```text
db.inventory.find( { status: "A" }, { status: 0, instock: 0 } )
```

> 返回嵌套在文档中指定的字段uom

```text
# 返回的数据
The _id field (returned by default),
The item field,
The status field,
The uom field in the size document.

db.inventory.find(
   { status: "A" },
   { item: 1, status: 1, "size.uom": 1 }
)
```

> 查询的文档字段instock数组中最后一个元素数据,使用mongodb的文档数组投影

```text
# $elemMatch, $slice, and $.
db.inventory.find( { status: "A" }, { item: 1, status: 1, instock: { $slice: -1 } } )
```

#### 查询Null或者不存在的字段

```text
## 数据准备
db.inventory.insertMany([
   { _id: 1, item: null },
   { _id: 2 }
])
```

> 查询item为null的文档数据

```text
db.inventory.find( { item: null } )
```

> 类型检查，bson数据为null的类型type是10

```text
db.inventory.find( { item : { $type: 10 } } )
```

> 字段存在性检查

```text
db.inventory.find( { item : { $exists: false } } )
```

#### mongodb shell迭代

> 手动迭代

```javascript 1.8
var myCursor = db.users.find( { type: 2 } );
myCursor
```

> 使用next迭代

```javascript 1.8
var myCursor = db.users.find( { type: 2 } );

while (myCursor.hasNext()) {
   printjson(myCursor.next());
}
```

> 使用foreach

```javascript 1.8
var myCursor =  db.users.find( { type: 2 } );

myCursor.forEach(printjson);
```

> 使用索引迭代

```text
var myCursor = db.inventory.find( { type: 2 } );
var documentArray = myCursor.toArray();
var myDocument = documentArray[3];
```

> 索引迭代与文档下标

```text
var myCursor = db.users.find( { type: 2 } );
var myDocument = myCursor[1];

## 等价于

myCursor.toArray() [1];
```

> 使用noCursorTimeout()将阻止cursor连接超时10min之后自动关闭

```text
var myCursor = db.users.find().noCursorTimeout();
```

> cursor batch操作

```text
# find() and aggregate() operations have an initial batch size of 101 documents by default
# cursor.next() will perform a getMore operation to retrieve the next batch
# To see how many documents remain in the batch as you iterate the cursor, you can use the objsLeftInBatch()
var myCursor = db.inventory.find();

var myFirstDocument = myCursor.hasNext() ? myCursor.next() : null;

myCursor.objsLeftInBatch();
```

> Cursor Information

```text
db.serverStatus().metrics.cursor
# 查询结果如下：
{
   "timedOut" : <number>
   "open" : {
      "noTimeout" : <number>,
      "pinned" : <number>,
      "total" : <number>
   }
}
```





