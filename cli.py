from agent.graph import graph

while True:
    q = input("VoltAI > ")

    result = graph.invoke({
        "question": q,
        "result": ""
    })

    print(result["result"])