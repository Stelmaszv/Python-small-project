import { Injectable } from '@angular/core';
import {Observable} from 'rxjs'
import { HttpClient,HttpHeaders } from '@angular/common/http'
import { List_Model } from '../model/list'

const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type': 'application/json'
  })
}
@Injectable({
  providedIn: 'root'
})
export class ListService {
  list:string = 'http://127.0.0.1:8000/list/';
  limit = '?_limit=5';
  constructor(private http:HttpClient) { }
  getList() :Observable<List_Model[]> {
      return this.http.get<List_Model[]>(this.list)
  }
  get(id) :Observable<any>{
    const url=`${this.list}${id}`
    return this.http.get<any>(url)
  }
  add(form){
    this.http.post(this.list,form)
  }
  delete(id){
    const url=`${this.list}/${id}`
    this.http.delete(url)
  }
}
