import React, { useState } from 'react'
import './styles.scss'

const LOWERCASE_MIN_IDX = 97
const LOWERCASE_MAX_IDX = 122
const UPPERCASE_MIN_IDX = 65
const UPPERCASE_MAX_IDX = 90
const CONST1 = 65
const CONST2 = 32

function App() {
	const [fileText, setFileText] = useState('')
	const [keyText, setKeyText] = useState('')
	const [crypredText, setCryptedText] = useState('')
	const [decryptedText, setDecryptedText] = useState('')

	const showFile = () => {
		if (window.File && window.FileReader && window.FileList && window.Blob) {
			const file = document.querySelector('input[type=file]').files[0]
			const reader = new FileReader()
			const textFile = /text.*/

			if (file.type.match(textFile)) {
				reader.onload = function (event) {
					setFileText(event.target.result)
				}
			} else {
				setFileText('It doesnt seem to be a text file')
			}
			reader.readAsText(file)
		} else {
			alert('Your browser is too old to support HTML5 File API')
		}
	}

	const isLowerCase = a => {
		return a >= LOWERCASE_MIN_IDX && a <= LOWERCASE_MAX_IDX
	}

	const isUpperCase = a => {
		return a >= UPPERCASE_MIN_IDX && a <= UPPERCASE_MAX_IDX
	}

	const isLetter = a => {
		return isLowerCase(a) || isUpperCase(a)
	}

	const keyIntoNumbersArray = keyText => {
		const array = []
		for (let i = 0; i < keyText.length; i++) {
			const c = keyText.charCodeAt(i)
			if (isLetter(c)) {
				array.push((c - CONST1) % CONST2)
			}
		}
		return array
	}

	const crypt = (text, key) => {
		let encrypted = ''
		for (let i = 0, j = 0; i < text.length; i++) {
			const c = text.charCodeAt(i)
			if (isUpperCase(c)) {
				encrypted += String.fromCharCode(
					((c - 65 + key[j % key.length]) % 26) + 65,
				)
				j++
			} else if (isLowerCase(c)) {
				encrypted += String.fromCharCode(
					((c - 97 + key[j % key.length]) % 26) + 97,
				)
				j++
			} else {
				encrypted += text.charAt(i)
			}
		}
		return encrypted
	}

	const doCrypt = isDecrypt => {
		if (keyText.length === 0) {
			console.log('Key is empty, please enter the key inside field')
			return ''
		}
		const keyArray = keyIntoNumbersArray(keyText)

		if (keyArray.length === 0) {
			console.log('Key has no letter, please enter key with letters')
			return ''
		}

		if (isDecrypt) {
			for (let i = 0; i < keyArray.length; i++) {
				keyArray[i] = (26 - keyArray[i]) % 26
			}
		}

		if (isDecrypt) {
			const decrypted = crypt(crypredText, keyArray)
			setDecryptedText(decrypted)
		} else {
			const crypted = crypt(fileText, keyArray)
			setCryptedText(crypted)
			setDecryptedText('')
		}
	}

	return (
		<div className='app'>
			<h1 className='app-title'>Informational systems security, lab1</h1>
			<h2 className='app-subtitle'>
				Completed by Zheleznova Valeriia, group DA-81
			</h2>
			<h3 className='app-description'>
				Please, upload the file to encrypt it using Vigenere-Cipher algorytm
			</h3>
			<input className='app-file-input' type='file' />
			<button className='app-input-button' onClick={showFile}>
				Upload file
			</button>
			{fileText && (
				<div className='app-file-content'>
					<p className='app-file-content__title'>Content of uploaded file:</p>
					<div className='app-file-content__container'>
						<p className='app-file-content__container-text'>{fileText}</p>
					</div>
				</div>
			)}
			<p className='app-inputkey'>Input your key</p>
			<input
				className='app-key'
				type='text'
				value={keyText}
				placeholder='Input key'
				onChange={e => setKeyText(e.target.value)}
			/>
			<button className='app-input-button' onClick={() => doCrypt(false)}>
				Encrypt
			</button>
			{crypredText && (
				<div className='app-file-content'>
					<p className='app-file-content__title'>
						Encrypted text with your key:
					</p>
					<div className='app-file-content__container'>
						<p className='app-file-content__container-text'>{crypredText}</p>
					</div>
				</div>
			)}
			<button className='app-input-button' onClick={() => doCrypt(true)}>
				Decrypt
			</button>
			{decryptedText && (
				<div className='app-file-content'>
					<p className='app-file-content__title'>Decrypted text:</p>
					<div className='app-file-content__container'>
						<p className='app-file-content__container-text'>{decryptedText}</p>
					</div>
				</div>
			)}
		</div>
	)
}

export default App
