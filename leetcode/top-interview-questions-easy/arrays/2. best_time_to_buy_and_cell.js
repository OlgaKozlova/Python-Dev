/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
  var oldPrice = prices[0];
  var profit = 0 - oldPrice;
  var bought = true;

  for (var day = 1; day < prices.length; day++) {
    var price = prices[day];
    if (bought) {
      if (price <= oldPrice) {
        //console.log('before day -', day, 'price - ', price, 'profit - ', profit, 'var - перекупить')
        // перекупить
        // отменяем предыдущую покупку аки не бывало
        profit = profit + oldPrice;
        // покупаем по новой цене
        oldPrice = prices[day];
        profit = profit - oldPrice;
        //console.log('after day -', day, 'price - ', price, 'profit - ', profit, 'var - перекупить')
      } else {
        //console.log('before day -', day, 'price - ', price, 'profit - ', profit, 'var - продать')
        // продать
        bought = false;
        oldPrice = prices[day];
        profit = profit + oldPrice;
        //console.log('after day -', day, 'price - ', price, 'profit - ', profit, 'var - продать')
      }
    } else {
      if (price >= oldPrice) {
        //console.log('before day -', day, 'price - ', price, 'profit - ', profit, 'var - перепродать')
        // перепродать
        // отменяем предыдущую продажу аки не бывало
        profit = profit - oldPrice;
        // продаем по новой цене
        oldPrice = prices[day];
        profit = profit + oldPrice;
        //console.log('after day -', day, 'price - ', price, 'profit - ', profit, 'var - перепродать')
      } else {
        //console.log('before day -', day, 'price - ', price, 'profit - ', profit, 'var - купить')
        // купить
        bought = true;
        oldPrice = prices[day];
        profit = profit - oldPrice;
        //console.log('after day -', day, 'price - ', price, 'profit - ', profit, 'var - купить')
      }
    }
  }

  if (bought) {
    // Отменяем покупку последнюю, если после нее не продали
    profit = profit + oldPrice;
  }

  return profit > 0 ? profit : 0;
};
