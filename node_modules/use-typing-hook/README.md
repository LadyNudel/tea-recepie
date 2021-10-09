# use-typing-hook

> Custom React Hook to help you create a typing text effect in you app.

[![NPM](https://img.shields.io/npm/v/use-typing-hook.svg)](https://www.npmjs.com/package/use-typing-hook) [![JavaScript Style Guide](https://img.shields.io/badge/code_style-standard-brightgreen.svg)](https://standardjs.com)

## Install

```bash
npm install --save use-typing-hook
```

## Usage

```jsx
import React, { Component } from 'react'

import useTyping from 'use-typing-hook'

const Example = () => {
  // useTyping accepts three parameter
  // 1. Text
  // 2. Minimum delay timing
  // 3. Maximum delay timing

  const typingText = useTyping("Hello useTyping!", 200, 400)
  return (
    <div>{typingText}</div>
  )
}
```

## License

MIT © [nnnkit](https://github.com/nnnkit)
