let n = parseInt(document.forms['CountForm']['count'].value, 10);
n =  n ? n : 0;

const start = () => {
    document.forms['CountForm']['count'].value=n;
}

const up = () => {
    if (n < 9)
        n += 1;
    document.forms['CountForm']['count'].value=n;
}

const down = () => {
    if (n > 0)
        n -= 1;
        document.forms['CountForm']['count'].value=n;
}

start()
