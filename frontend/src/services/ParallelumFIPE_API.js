import axios from 'axios'

const API_BASE_URL = 'https://parallelum.com.br/fipe/api/v1'

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json'
  }
})

const getBrandCode = async (targetBrand) => {
  const response = await apiClient.get('/carros/marcas')

  const brandCode = response.data.find(
    (brand) => {
      const brandName = brand.nome.includes(' - ') ? brand.nome.split(' - ')[1] : brand.nome
      return brandName.toLowerCase() === targetBrand.toLowerCase()
    }
  )?.codigo

  return brandCode
}

const getModelCode = async (brandCode, targetModel) => {
  const response = await apiClient.get(`/carros/marcas/${brandCode}/modelos`)

  const modelCode = response.data.modelos.find(
    (model) => model.nome.toLowerCase() === targetModel.toLowerCase()
  )?.codigo

  return modelCode
}

const getModelYearCode = async (brandCode, modelCode, targetYear) => {
  const response = await apiClient.get(`/carros/marcas/${brandCode}/modelos/${modelCode}/anos`)

  const yearCode = targetYear
    ? response.data?.find((year) => year.nome.includes(targetYear))?.codigo
    : response.data?.[0]?.codigo

  return yearCode
}

const getFipePriceAndDate = async (brandCode, modelCode, yearCode) => {
  const response = await apiClient.get(
    `/carros/marcas/${brandCode}/modelos/${modelCode}/anos/${yearCode}`
  )

  return {
    price: response.data.Valor,
    date: response.data.MesReferencia
  }
}

/**
 * * Fetches the most recent car FIPE price using the Parallelum free and open-source API.
 * * API Documentation: https://deividfortuna.github.io/fipe/
 */
export const getFipeFromParallelum = async (brand, model, year, outdatedPrice) => {
  try {
    const defaultFipeData = {
      price: outdatedPrice,
      warning: 'Desculpe, não encontramos um valor atualizado. O valor mostrado pode não refletir o preço atual do veículo.' 
    }

    if (import.meta.env.DEV === true) {
      return defaultFipeData
    }

    const brandCode = await getBrandCode(brand)
    if (!brandCode) {
      return defaultFipeData
    }

    const modelCode = await getModelCode(brandCode, model)
    if (!modelCode) {
      return defaultFipeData
    }

    const yearCode = await getModelYearCode(brandCode, modelCode, year)
    if (!yearCode) {
      return defaultFipeData
    }

    const fipeData = await getFipePriceAndDate(brandCode, modelCode, yearCode)
    if (!fipeData) {
      return defaultFipeData
    }

    return fipeData
  } catch (error) {
    console.error('getFipe error:', error)
    throw error
  }
}
