import { Injectable } from '@angular/core';
import {Observable} from 'rxjs'
import { HttpClient,HttpHeaders } from '@angular/common/http'
import { List_Model } from '../model/list'

@Injectable({
  providedIn: 'root'
})
export class ListService {
  list:string = 'https://jsonplaceholder.typicode.com/todos';
  limit = '?_limit=5';
  constructor(private http:HttpClient) { }
  getList() :Observable<List_Model[]> {
      return this.http.get<List_Model[]>(`${this.list}${this.limit}`)
  }

}
