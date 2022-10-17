import React from 'react';


export default class App extends React.Component{
  //прописываем исходное состояние
  state ={
    count: 0,
    isCounting: false
  };

// при старте переводим isCounting в значение true, запускаем таймер
// функция setInterval каждую секунду увеличивает count на 1
handelStart = () => {
  this.setState({isCounting: true});
  this.couterId = setInterval(() => {
    this.setState({ count: this.state.count + 1 });
  }, 1000);
};

// при остановке переводим isCounting в значение false, останавливаем таймер
handelStop = () => {
  this.setState({ isCounting: false });
// в функцию clearInterval передаём couterId из handelStart
  clearInterval(this.couterId);
};

// при сбросе приводим таймер в начальное состояние
handelReset = () => {
  this.setState({isCounting: false, count: 0 });
  clearInterval(this.couterId);
};


// вносим значение в localStorage
componentDidUpdate() {
  localStorage.setItem('timer', this.state.count)
}

// вынимаем значение из localStorage
componentDidMount() {
  const userCount = localStorage.getItem('timer');
  //пишем условие если в count есть значение
  // +userCount - + переводит строку в число
  if (userCount) {
    this.setState({ count: +userCount });
  }
}



// если пользователь ушёл со страницы и не остановил таймер, останавливаем его
componentWillUnmount() {
  clearInterval(this.counterId);
}


render() {
  return (
    <div className="App">
    <h1>Timer</h1>
    <h3>{this.state.count}</h3>
    {/* условие если таймер остановлен показываем Start если запущен Stop */}
    {!this.state.isCounting ? (
      <button onClick={this.handelStart}>Start</button>
    ) : (
      <button onClick={this.handelStop}>Stop</button>
    )}
      <button onClick={this.handelReset}>Reset</button>
    </div>
    );
 }
}


// npm start
